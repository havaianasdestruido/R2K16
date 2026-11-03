package com.roblox.client.http;

import java.io.ByteArrayOutputStream;
import java.io.UnsupportedEncodingException;

public class HttpResponse {
    enum RequestType { GET, POST };
    public RequestType requestType;
    private String mResponseString = null;
    String mUrl = null;
    private byte[] mResponseRaw = null;
    int mResponseCode;
    long mResponseTime = 0l;

    // Only used by HttpAgent, so it's package-private
    void setResponseBody(ByteArrayOutputStream boas) {
        mResponseRaw = boas.toByteArray();
        try {
            mResponseString = new String(mResponseRaw, "UTF-8");
        }
        catch (UnsupportedEncodingException e) {
            e.printStackTrace();
            mResponseString = "";
        }
    }

    /***
     * The response body as a string. If the response was empty, an empty string will be returned.
     * @return Response body as string
     */
    public String responseBodyAsString() { return (mResponseString == null ? "" : mResponseString); }

    /***
     * The response body as an array of bytes. If the response was empty, an empty array will be returned.
     * @return Response body as byte array
     */
    public byte[] responseBodyAsBytes() { return mResponseRaw; }

    public int responseCode() { return mResponseCode; }
    public String url() { return mUrl; }

    @Override
    public String toString() {
        // HttpResponse is logged by several callers. A full URL can contain an
        // apiKey/password in its query string and the body can contain session
        // data, so expose only non-sensitive metadata here.
        return "HTTP Response for URL: " + HttpAgent.safeUrlForLog(mUrl) + "\n" +
                "Request Type: " + requestType + "\n" +
                "Response Code: " + mResponseCode;
    }

    public long responseTime() { return mResponseTime; }
}
