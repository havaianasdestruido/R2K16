package com.roblox.client;

import android.content.Context;
import android.content.SharedPreferences;
import android.util.Base64;

import java.security.MessageDigest;
import java.security.SecureRandom;
import java.util.Arrays;

import javax.crypto.Cipher;
import javax.crypto.Mac;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

/**
 * Protects the small number of values the client persists locally (currently the
 * "remember me" password in {@link com.roblox.client.managers.SessionManager}).
 *
 * <p>The old implementation used {@code PBEWithMD5AndDES} with a password and salt
 * derived from a fixed-seed xorshift generator that was compiled into the APK. Both
 * DES and MD5 are broken, and the key material was identical on every device, so the
 * "encryption" was reversible by anyone holding the app. It also silently returned
 * its input when crypto failed, which could persist a plaintext password.</p>
 *
 * <p>This implementation uses AES-256/CBC with a random IV and an encrypt-then-MAC
 * HMAC-SHA256 tag, keyed with a per-install 512-bit master secret generated with
 * {@link SecureRandom} and kept in a private {@link SharedPreferences} file. It works
 * on the whole supported API range (minSdkVersion 15); no key is compiled into the app.
 * Values written by the old scheme are intentionally NOT decrypted: they are treated
 * as invalid and the user is asked to sign in again.</p>
 */
public final class ConfigEncryption {

    private static final String PREFS_NAME = "r2k16_config_encryption";
    private static final String MASTER_KEY_PREF = "master_key";
    private static final String VERSION_PREFIX = "v2:";

    private static final String CIPHER_TRANSFORMATION = "AES/CBC/PKCS5Padding";
    private static final String MAC_ALGORITHM = "HmacSHA256";
    private static final String CHARSET = "UTF-8";

    private static final int AES_KEY_BYTES = 32;   // AES-256
    private static final int MAC_KEY_BYTES = 32;
    private static final int MASTER_KEY_BYTES = AES_KEY_BYTES + MAC_KEY_BYTES;
    private static final int IV_BYTES = 16;
    private static final int MAC_BYTES = 32;

    // Keep padding enabled so Base64.decode() accepts the output on every API level.
    private static final int BASE64_FLAGS = Base64.NO_WRAP;

    private ConfigEncryption() {
    }

    /**
     * Encrypts a value for local storage. Returns an empty string when encryption
     * cannot be performed; callers must never persist the plaintext in that case.
     */
    public static String encrypt(String property) {
        if (property == null || property.isEmpty()) {
            return "";
        }

        Context context = RobloxApplication.getInstance();
        if (context == null) {
            // Fail closed: never write a secret we cannot protect.
            return "";
        }

        try {
            byte[] masterKey = getOrCreateMasterKey(context);
            byte[] plaintext = property.getBytes(CHARSET);

            byte[] iv = new byte[IV_BYTES];
            new SecureRandom().nextBytes(iv);

            Cipher cipher = Cipher.getInstance(CIPHER_TRANSFORMATION);
            cipher.init(Cipher.ENCRYPT_MODE, aesKey(masterKey), new IvParameterSpec(iv));
            byte[] ciphertext = cipher.doFinal(plaintext);

            // Layout: IV || ciphertext || HMAC(IV || ciphertext)
            byte[] payload = new byte[IV_BYTES + ciphertext.length + MAC_BYTES];
            System.arraycopy(iv, 0, payload, 0, IV_BYTES);
            System.arraycopy(ciphertext, 0, payload, IV_BYTES, ciphertext.length);

            byte[] mac = computeMac(masterKey, payload, IV_BYTES + ciphertext.length);
            System.arraycopy(mac, 0, payload, IV_BYTES + ciphertext.length, MAC_BYTES);

            return VERSION_PREFIX + Base64.encodeToString(payload, BASE64_FLAGS);
        } catch (Exception e) {
            // Deliberately no logging: exceptions here can carry secret material.
            return "";
        }
    }

    /**
     * Decrypts a value produced by {@link #encrypt(String)}. Returns an empty string
     * for absent, legacy, tampered or otherwise invalid input.
     */
    public static String decrypt(String property) {
        if (property == null || property.isEmpty() || !property.startsWith(VERSION_PREFIX)) {
            // Legacy PBEWithMD5AndDES values are deliberately discarded rather than
            // decrypted with the publicly known, broken key.
            return "";
        }

        Context context = RobloxApplication.getInstance();
        if (context == null) {
            return "";
        }

        try {
            byte[] payload = Base64.decode(property.substring(VERSION_PREFIX.length()), BASE64_FLAGS);
            int ciphertextLength = payload.length - IV_BYTES - MAC_BYTES;
            if (ciphertextLength <= 0) {
                return "";
            }

            byte[] masterKey = getOrCreateMasterKey(context);
            byte[] expectedMac = computeMac(masterKey, payload, IV_BYTES + ciphertextLength);
            byte[] actualMac = Arrays.copyOfRange(payload, IV_BYTES + ciphertextLength, payload.length);
            if (!MessageDigest.isEqual(expectedMac, actualMac)) {
                // Authenticate before decrypting: reject modified or forged values.
                return "";
            }

            Cipher cipher = Cipher.getInstance(CIPHER_TRANSFORMATION);
            cipher.init(Cipher.DECRYPT_MODE, aesKey(masterKey),
                    new IvParameterSpec(payload, 0, IV_BYTES));
            byte[] plaintext = cipher.doFinal(payload, IV_BYTES, ciphertextLength);
            return new String(plaintext, CHARSET);
        } catch (Exception e) {
            return "";
        }
    }

    private static byte[] getOrCreateMasterKey(Context context) {
        SharedPreferences prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE);
        String stored = prefs.getString(MASTER_KEY_PREF, null);
        if (stored != null) {
            try {
                byte[] key = Base64.decode(stored, BASE64_FLAGS);
                if (key.length == MASTER_KEY_BYTES) {
                    return key;
                }
            } catch (IllegalArgumentException ignored) {
                // Corrupt key material: generate a fresh one below.
            }
        }

        byte[] key = new byte[MASTER_KEY_BYTES];
        new SecureRandom().nextBytes(key);
        // commit() so the key is durable before any ciphertext is written with it.
        prefs.edit().putString(MASTER_KEY_PREF, Base64.encodeToString(key, BASE64_FLAGS)).commit();
        return key;
    }

    private static SecretKeySpec aesKey(byte[] masterKey) {
        return new SecretKeySpec(Arrays.copyOfRange(masterKey, 0, AES_KEY_BYTES), "AES");
    }

    private static byte[] computeMac(byte[] masterKey, byte[] data, int length) throws Exception {
        Mac mac = Mac.getInstance(MAC_ALGORITHM);
        mac.init(new SecretKeySpec(
                Arrays.copyOfRange(masterKey, AES_KEY_BYTES, MASTER_KEY_BYTES), MAC_ALGORITHM));
        mac.update(data, 0, length);
        return mac.doFinal();
    }
}
