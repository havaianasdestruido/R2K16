package com.roblox.client;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

import android.content.Context;
import android.util.Log;

public class XAPKManager
{
    private static String TAG = "roblox.xapkmanager";

    private static String ASSET_CONTAINER_FILENAME = "main.1.com.roblox.client.obb";
    private static String FINGERPRINT_FILENAME = "fingerprint.txt";
    private static int BUFFER_SIZE = 8192;

    // Upper bounds for the (untrusted) OBB archive. Without these a malformed or
    // hostile container can exhaust storage/CPU (zip bomb) even with safe paths.
    private static final int MAX_ZIP_ENTRIES = 10000;
    private static final long MAX_UNCOMPRESSED_BYTES = 1024L * 1024L * 1024L; // 1 GiB

    private static final Lock mLock = new ReentrantLock();
    private static String mCachedAssetPath = null;

    /**
     * Unpacks the assets from the obb/zip file
     * @param context A context for accessing assets, paths, etc
     *        If assets are already unpacked, its a no-op.
     *
     * @return A string representing the path to the uncompressed assets
     */
    public static void unpackAssetsAsync(final Context context)
    {
        Runnable runnable = new Runnable()
        {
            @Override
            public void run()
            {
                unpackAssets(context);
            }
        };
        new Thread(runnable).start();
    }

    /**
     * Unpacks the assets from the obb/zip file
     * @param context A context for accessing assets, paths, etc
     *        If assets are already unpacked, its a no-op.
     *
     * @return A string representing the path to the uncompressed assets
     */
    public static String unpackAssets(final Context context)
    {
        mLock.lock();
        try
        {
            if(mCachedAssetPath == null)
            {
                final File baseAssetPath = context.getDir("assets", Context.MODE_PRIVATE);
            	
                String obbFingerprint = readOBBFingerprint(context);
                String assetsFingerprint = readAssetsFingerprint(baseAssetPath.toString());

                if (assetsFingerprint != null && obbFingerprint != null) {
                    if (assetsFingerprint.isEmpty() || !obbFingerprint.equals(assetsFingerprint)) {
                        if (!obbFingerprint.isEmpty()) {
                            // Empty the folder first
                            baseAssetPath.delete();
                            baseAssetPath.mkdirs();

                            unzipContainer(context, baseAssetPath.toString());
                            writeFingerprint(obbFingerprint, baseAssetPath.toString());
                        } else if (assetsFingerprint.isEmpty()) {
                            Log.e(TAG, "Unable to reach a valid OBB file. Assets are not available");
                        }
                    } else {
                        Log.v(TAG, "Assets are up to date");
                    }
                }
                else
                    Log.e(TAG, "assetsFingerprint or obbFingerprint null - assets were not packaged into build.");

                mCachedAssetPath = baseAssetPath + "/content";
            }
        }
        finally
        {
            mLock.unlock();
        }

        return mCachedAssetPath;
    }
    
    private static String readOBBFingerprint(Context context)
    {
    	String fingerprint = null;
    	
    	InputStream inputStream = null;
    	BufferedReader bufferReader = null;
    	try
    	{
    		inputStream = context.getAssets().open(FINGERPRINT_FILENAME);
    		bufferReader = new BufferedReader(new InputStreamReader(inputStream));
    		fingerprint = bufferReader.readLine();
    		bufferReader.close();
    		inputStream.close();
    	}
    	catch (IOException e)
    	{
    		Log.e(TAG, "Exception: " + e.getMessage());
    	}
    	finally
    	{
    		try
    		{
    			if (bufferReader != null)
    				bufferReader.close();
    			
    			if (inputStream != null)
    				inputStream.close();
    		}
    		catch (IOException ignored)
    		{
    	    }
    		
    		bufferReader = null;
    	    inputStream = null;
    	}
    	
    	return fingerprint;
    }

    private static String readAssetsFingerprint(final String baseAssetPath)
    {
        String fingerprint = "";
        File file = new File(baseAssetPath, FINGERPRINT_FILENAME);

        BufferedReader reader=null;
        try
        {
            reader = new BufferedReader(new FileReader(file));
            fingerprint = reader.readLine();
        }
        catch (IOException e)
        {
        }
        finally
        {
            try
            {
                if(reader != null)
            	   reader.close();
            }
            catch (IOException e)
            {
            }
        }
        
        return fingerprint;
    }

    /**
     * Zip Slip guard: an archive entry must resolve to a file inside baseDir.
     * This rejects absolute paths, Windows drive letters, backslash separators,
     * ".." traversal and entries that escape through an existing symlink.
     */
    private static boolean isSafeDestination(File baseDir, String entryName) throws IOException
    {
        if (entryName == null || entryName.isEmpty()
                || entryName.startsWith("/") || entryName.startsWith("\\")
                || entryName.indexOf('\\') >= 0 || entryName.indexOf('\0') >= 0)
        {
            return false;
        }

        String base = baseDir.getCanonicalPath();
        if (!base.endsWith(File.separator))
        {
            base += File.separator;
        }
        return new File(baseDir, entryName).getCanonicalPath().startsWith(base);
    }

    private static void unzipContainer(Context context, final String baseAssetPath)
    {
        int size;
        byte[] buffer = new byte[BUFFER_SIZE];
        long totalBytes = 0;
        int entryCount = 0;

        try
        {
            final File baseDir = new File(baseAssetPath);
        	InputStream inputStream = new BufferedInputStream( context.getAssets().open(ASSET_CONTAINER_FILENAME) );
            ZipInputStream zin = new ZipInputStream(inputStream);
            try
            {
                ZipEntry ze = null;
                while((ze = zin.getNextEntry()) != null)
                {
                    if (++entryCount > MAX_ZIP_ENTRIES)
                    {
                        Log.e(TAG, "Aborting unzip: too many entries");
                        break;
                    }

                    if (!isSafeDestination(baseDir, ze.getName()))
                    {
                        // Never create a file outside the private asset directory.
                        // Log only the (untrusted) name, not any local absolute path.
                        Log.e(TAG, "Skipping unsafe zip entry name");
                        continue;
                    }

                    File unzipFile = new File(baseDir, ze.getName());

                    if( ze.isDirectory() )
                    {
                        if( !unzipFile.isDirectory() )
                        {
                            unzipFile.mkdirs();
                        }
                    }
                    else
                    {
                        // Check for and create parent directories if they don't exist
                        File parentDir = unzipFile.getParentFile();
                        if( null != parentDir )
                        {
                            if( !parentDir.isDirectory() )
                            {
                                parentDir.mkdirs();
                            }
                        }

                        // Unzip the file
                        FileOutputStream out = new FileOutputStream(unzipFile, false);
                        BufferedOutputStream fout = new BufferedOutputStream(out, BUFFER_SIZE);
                        try
                        {
                            while ( (size = zin.read(buffer, 0, BUFFER_SIZE)) != -1 )
                            {
                                totalBytes += size;
                                if (totalBytes > MAX_UNCOMPRESSED_BYTES)
                                {
                                    throw new IOException("Uncompressed asset size limit exceeded");
                                }
                                fout.write(buffer, 0, size);
                            }

                            zin.closeEntry();
                        }
                        finally
                        {
                            fout.flush();
                            fout.close();
                        }
                    }
                }
            }
            finally
            {
                zin.close();
            }
        }
        catch (Exception e)
        {
            Log.e(TAG, "Unzip exception", e);
        }
    }
    
    private static void writeFingerprint(final String fingerprint, final String baseAssetPath)
    {
    	OutputStream out = null;
    	try
    	{
	        out = new FileOutputStream( new File(baseAssetPath + "/" + FINGERPRINT_FILENAME) );
	        out.write(fingerprint.getBytes());
	        out.close();
    	}
    	catch (Exception e)
    	{
    		Log.e(TAG, "Exception " + e.getMessage());
    	}
    	finally
    	{
    		try
    		{
	    		if(out != null)
	    			out.close();
    		}
    		catch(Exception ignored)
    		{}
    	}
    }
}
