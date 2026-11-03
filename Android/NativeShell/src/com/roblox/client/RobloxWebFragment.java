package com.roblox.client;

import android.app.Activity;
import android.app.DialogFragment;
import android.content.Context;
import android.content.DialogInterface;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.support.v4.widget.SwipeRefreshLayout;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewGroup;
import android.view.Window;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.webkit.*;
import android.widget.Toast;

import com.roblox.client.http.HttpAgent;
import com.roblox.client.http.HttpResponse;
import com.roblox.client.http.OnRbxHttpRequestFinished;
import com.roblox.client.http.RbxHttpGetRequest;
import com.roblox.client.managers.NotificationManager;
import com.roblox.client.managers.SessionManager;

import org.json.JSONArray;
import org.json.JSONObject;

import java.text.NumberFormat;

public class RobloxWebFragment extends DialogFragment implements NotificationManager.Observer, SwipeRefreshLayout.OnRefreshListener {

	private static final String TAG = "RobloxWebFragment";

	private TextView mUrlBar = null;
	private WebView mWebView = null;
	private String mPlaceId = null;
	private WebViewClientEmbedded mWebViewClientEmbedded = null;
    private SwipeRefreshLayout mRefreshLayout = null;
    private String mURLToLoad = null;
    float m_downX, m_downY = 0;
    private int mDialogHeight = 0;
    private boolean isRobuxDialog, isBCDialog, isCaptchaDialog, isSocialCaptcha = false;
    private String mDefaultUrl = null;
    private WebviewInterface mWebviewInterface = null;
    private boolean mUseCompat = false;

    public static final String FRAGMENT_TAG_CAPTCHA = "captcha_window";

    private static final String JS_BRIDGE_NAME = "interface";
    private static final String TRUSTED_ASSET_PREFIX = "file:///android_asset/html/";

    /**
     * The JS bridge exposes native methods (launch game, open settings, ...). It
     * must only be reachable from the two local "more" pages shipped in the APK,
     * never from arbitrary web content reached through a link or redirect.
     */
    private boolean isTrustedBridgeUrl(String url) {
        if (url == null || !url.startsWith(TRUSTED_ASSET_PREFIX)) {
            return false;
        }
        String name = url.substring(TRUSTED_ASSET_PREFIX.length()).split("[?#]")[0];
        return name.equals("more.html") || name.equals("more_phone.html");
    }

    /** Adds/removes the bridge so it is never exposed to untrusted documents. */
    private void syncJavascriptInterface(String url) {
        if (mWebView == null) {
            return;
        }
        boolean allowed = Build.VERSION.SDK_INT >= Build.VERSION_CODES.JELLY_BEAN_MR1
                && isTrustedBridgeUrl(url);
        if (allowed) {
            if (mWebviewInterface == null) {
                mWebviewInterface = new WebviewInterface(getActivity(), mUseCompat, mWebView);
            }
            mWebView.addJavascriptInterface(mWebviewInterface, JS_BRIDGE_NAME);
        } else {
            // removeJavascriptInterface() is available on every supported API.
            mWebView.removeJavascriptInterface(JS_BRIDGE_NAME);
            mWebviewInterface = null;
        }
    }

    // ------------------------------------------------------------------------
    private class WebViewClientEmbedded extends WebViewClient {

        @Override
        public void onPageStarted(WebView view, String url, Bitmap favicon) {
            mRefreshLayout.setRefreshing(true);
        }

        @Override
        public void onPageFinished(android.webkit.WebView view, java.lang.String url) {
            mRefreshLayout.setRefreshing(false);
            // Covers every navigation path (redirects, history back/forward and
            // direct loadUrl calls) so the bridge is never left exposed on a
            // document that is not one of our packaged local pages.
            syncJavascriptInterface(url);
        }

    	// Mirrors iOS: -(BOOL) checkForGameLaunch:(NSURLRequest *)request
    	@Override
        public boolean shouldOverrideUrlLoading(WebView view, String urlString) {
            // URLs can carry session ids / api keys in their query string.
            Log.i(TAG, "-> " + HttpAgent.safeUrlForLog(urlString));

            // The native JS bridge is only for the trusted local "more" pages.
            // Any link/redirect to web content must drop it immediately.
            syncJavascriptInterface(urlString);

    		if( Utils.alertIfNetworkNotConnected() )
    		{
    			return true;
    		}

            if (urlString != null && (urlString.contains("more.html") || urlString.contains("more_phone.html")))
            {
                mWebView.setOnTouchListener(new View.OnTouchListener() {
                    @Override
                    public boolean onTouch(View v, MotionEvent event) {
                        // Disables scrolling (on both axes) on webviews
                        switch (event.getAction()) {
                            case MotionEvent.ACTION_DOWN:
                                m_downX = event.getX();
                                m_downY = event.getY();
                                break;
                            case MotionEvent.ACTION_UP:
                                event.setLocation(m_downX, m_downY);
                                break;

                        }
                        return (event.getAction() == MotionEvent.ACTION_MOVE);
                    }
                });
            }
            else if (urlString.equals(RobloxSettings.captchaSolvedUrl()))
            {
                if (isSocialCaptcha)
                    NotificationManager.getInstance().postNotification(NotificationManager.EVENT_USER_CAPTCHA_SOCIAL_SOLVED);
                else
                    NotificationManager.getInstance().postNotification(NotificationManager.EVENT_USER_CAPTCHA_SOLVED);
                return true;
            }
            else if (AndroidAppSettings.EnableShellLogoutOnWebViewLogout() && RobloxSettings.isLoginRequiredWebUrl(urlString)) {
                // in case we somehow get logged out while in a webview
                Context context = getActivity();
                if(context != null) {
                    int duration = Toast.LENGTH_SHORT;
                    Toast toast = Toast.makeText(context, R.string.sessionExpiredLoginAgain, duration);
                    toast.show();
                }

                SessionManager.getInstance().doLogout();
                return true;
            }
            else
            {
                mWebView.setOnTouchListener(null);
            }

            shouldEnableZoom(urlString, true);

            RobloxApplication app = RobloxApplication.getInstance();
			if( app.checkShowCriticalError() )
			{
	        	Log.i(TAG, "Trying to use WebView after critical error.");
	        	return true;
			}

			Utils.sendAnalytics( "WebView", urlString );

        	if( urlString.indexOf( "/games/start?" ) > -1 )
           	{
        		String reason = RobloxSettings.deviceNotSupportedString();
        		if( reason != null && AndroidAppSettings.EnableNeonBlocker() )
        		{
            		if( !RobloxSettings.deviceNotSupportedSkippable() )
            		{
            			Utils.alertExclusivelyFormatted( R.string.UnsupportedDevice, reason );
            			return true;
            		}
        		}


                String accessId = null;
                String gameInstanceId = null;
                String userId = null;
                // 0 = Simple PlaceId join (placeId only)
                // 1 = Follow user join (by userId only)
                // 2 = Private server join (placeId & accessCode)
                // 3 = Game instance join (placeId & gameId)
                int requestType = -1;

                Uri uriObject = Uri.parse(urlString);
                mPlaceId = uriObject.getQueryParameter("placeid");
        		if( mPlaceId == null )
        		{
            		userId = uriObject.getQueryParameter("userID");
            		if( mPlaceId == null && userId == null)
            		{
            			Utils.alertUnexpectedError( "Missing placeid and userID." );
            			return true;
            		}
                    requestType = 1; // user follow
        		}
                else  if (mPlaceId != null && userId == null ) { // if we have a userId, we won't get either of these params
                    // if we have a placeId we don't /need/ anything else,
                    // but we might have a second parameter for the Private Server ID or Game Instance Id.
                    // Of these parameters, we may only use 1.

                    accessId = uriObject.getQueryParameter("accessCode");
                    if (accessId == null)
                    {
                        gameInstanceId = uriObject.getQueryParameter("gameInstanceId");
                        if (gameInstanceId == null)
                            requestType = 0; // simple game join
                        else
                            requestType = 3; // game instance join
                    }
                    else
                    {
                        requestType = 2; // private server join
                    }
                }

                if (requestType == -1)
                {
                    Log.e(TAG, "Game join request type not set.");
                    Utils.alert("Error joining game - could not determine join type.");
                    return false;
                }

        		Log.i(TAG, Utils.format( "Signalling Service PlaceId:%s", mPlaceId ) );

                RobloxActivity robloxActivity = (RobloxActivity) getActivity();
                UpgradeCheckHelper.UpgradeStatus status = UpgradeCheckHelper.showUpdateDialogIfRequired(robloxActivity);

        		if( status != UpgradeCheckHelper.UpgradeStatus.Recommended
        			&& status != UpgradeCheckHelper.UpgradeStatus.Required)
        		{
                    Bundle userParams = new Bundle();
                    if (mPlaceId != null)
                        userParams.putInt("placeId", Integer.parseInt(mPlaceId));
                    else
                    {
                        userParams.putInt("placeId", 0);

                        if (userId != null)
                            userParams.putInt("userId", Integer.parseInt(userId));
                        else
                            userParams.putInt("userId", 0);
                    }

                    userParams.putString("accessCode", accessId);
                    userParams.putString("gameId", gameInstanceId);
                    userParams.putInt("requestType", requestType);

                    // All this data ends up in JNIGLActivity.cpp:nativeStartGame

                    NotificationManager.getInstance().postNotification(NotificationManager.REQUEST_START_PLACEID, userParams);
        		}


                return true;
        	}
        	else if( urlString.indexOf( "mobile-app-upgrades/buy?" ) > -1 )
        	{
                RobloxActivity activity = (RobloxActivity) getActivity();
                StoreManager storeManager = activity.getStoreManager();
        		if(storeManager == null)
        		{
        			Utils.alertExclusively("Please upgrade your Android Version to allow Purchasing");
    				Utils.sendAnalytics("WebView", urlString + "/PurchaseFailedDueToOldAndroidVersion" );
        		}
        		else
        		{
                    Uri uriObject = Uri.parse(urlString);
                    String productId = uriObject.getQueryParameter("id");
                    RbxAnalytics.fireButtonClick(getDialogContext(), "purchaseStart" + productId);

                    RobloxSettings.getKeyValues().edit().putBoolean("isReturningFromPurchase", true).apply();

                    String username = SessionManager.getInstance().getUsername();
        			if(!storeManager.doInAppPurchaseForUrl(activity, urlString, username))
        			{
        				Utils.alertExclusively("Please setup Google Play Store to make purchases.");
        				Utils.sendAnalytics( "StoreManager", "PurchaseFailedDueToGooglePlayStoreNotSetup" );
        			}
        		}
        		return true;
        	}

        	mUrlBar.setText( urlString );
            view.loadUrl( urlString );

            return true;
        }
    }

    private void shouldEnableZoom(String urlString, boolean enableOrDisable) {
        if (!AndroidAppSettings.EnableSponsoredZoom()) return;
         
        if (urlString.contains("sponsored"))
            mWebView.getSettings().setBuiltInZoomControls(enableOrDisable); // if this suddenly stops working, check webView.setSupportZoom
        else
            mWebView.getSettings().setBuiltInZoomControls(!enableOrDisable);
    }


    // ------------------------------------------------------------------------
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_webview, container, false);

		mUrlBar = (TextView)view.findViewById(R.id.webview_urlbar);

        mWebViewClientEmbedded = new WebViewClientEmbedded();
        mWebView = (WebView)view.findViewById(R.id.web_view);
        mWebView.setWebViewClient(mWebViewClientEmbedded);
        mWebView.getSettings().setJavaScriptEnabled(true);
		mWebView.getSettings().setUserAgentString(RobloxSettings.userAgent());
		mWebView.getSettings().setCacheMode(WebSettings.LOAD_DEFAULT); // LOAD_CACHE_ONLY

        // A local HTML page must not be able to read arbitrary files or make
        // cross-origin requests. These are the dangerous defaults on old WebViews.
        mWebView.getSettings().setAllowContentAccess(false);
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.JELLY_BEAN) {
            mWebView.getSettings().setAllowFileAccessFromFileURLs(false);
            mWebView.getSettings().setAllowUniversalAccessFromFileURLs(false);
        }
        mWebView.setHorizontalScrollBarEnabled(false);
        mWebView.setVerticalScrollBarEnabled(false);

        // To find the device's default user agent, we can set it to null - just make sure to reset it afterwards
        String tempUA = mWebView.getSettings().getUserAgentString();
        mWebView.getSettings().setUserAgentString(null);
        String defaultUA = mWebView.getSettings().getUserAgentString();
        mWebView.getSettings().setUserAgentString(tempUA);
        mUseCompat = !defaultUA.contains("Chrome/");

        if(mURLToLoad != null) {
            // Decide from an exact trusted-URL match, not a substring test:
            // "https://evil.example/more.html?x=1" must not get the bridge.
            syncJavascriptInterface(mURLToLoad);
            mWebView.loadUrl(mURLToLoad);
            mURLToLoad = null;
        }

        mRefreshLayout = (SwipeRefreshLayout) view.findViewById(R.id.swipe_container);
        mRefreshLayout.setOnRefreshListener(this);
        mRefreshLayout.setColorSchemeResources(R.color.RbxRed1, R.color.RbxRed1, R.color.white, R.color.white);
//        mRefreshLayout.setColorScheme(android.R.color.holo_purple,
//                R.color.RbxBlue1,
//                R.color.RbxGreen1,
//                R.color.RbxOrange);

        // These should only exist when we're creating one of our DialogWebFragments
        Bundle args = getArguments();
        if (args != null)
        {
            if (args.getBoolean("showRobux", false))
            {
                SessionManager sm = SessionManager.getInstance();
                getDialog().setTitle("Current Balance: R$ " + NumberFormat.getIntegerInstance().format(sm.getRobuxBalance()));
                isRobuxDialog = true;
            }
            else if (args.getBoolean("showBC", false))
                isBCDialog = true;
            else if (args.getBoolean("showCaptcha", false)) {
                isCaptchaDialog = true;
                if (args.getBoolean("isSocial", false))
                    isSocialCaptcha = true;
            }


            mDialogHeight = args.getInt("dialogHeight", 0);
            if (!args.getBoolean("enablePullToRefresh", true))
                mRefreshLayout.setEnabled(false);
        }

		mUrlBar.setVisibility( RobloxSettings.isInternalBuild() ? View.VISIBLE : View.GONE);

		Utils.alertIfNetworkNotConnected();

        // Remote WebView debugging exposes the DOM/cookies to anyone with ADB
        // access. Keep it for internal builds only.
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {
            mWebView.setWebContentsDebuggingEnabled(RobloxSettings.isInternalBuild());
        }

        return view;
	}

    // ------------------------------------------------------------------------
    @Override
    public void onResume() {
        super.onResume();

        NotificationManager.getInstance().addObserver(this);

        if (getDialog() != null && mDialogHeight != 0) // resizes the window - have to put it here, because the dialog
                                // isn't available yet in onCreate
        {
            Window window = getDialog().getWindow();
            window.setLayout(LinearLayout.LayoutParams.WRAP_CONTENT, mDialogHeight);
        }
    }


    // ------------------------------------------------------------------------
	@Override
	public void onPause()
	{
		super.onPause();

        NotificationManager.getInstance().removerObserver(this);
	}

    // ------------------------------------------------------------------------
    @Override
    public void handleNotification(int notificationId, Bundle userParams) {
        switch (notificationId) {
            case NotificationManager.EVENT_USER_LOGIN:
                mWebView.reload();
                break;
            case NotificationManager.EVENT_USER_LOGOUT:
                if(AndroidAppSettings.EnableSetWebViewBlankOnLogout()) {
                    // User logged out, stop the webview from continuing to run stuff in the background (happens on some devices)
                    mWebView.loadUrl("about:blank");
                }
                break;

            default:
                break;
        }
    }

    // ------------------------------------------------------------------------
    @Override
    public void onRefresh() {
        mWebView.reload();
    }

    // ------------------------------------------------------------------------
    public void loadURL(final String url) {
        if(mWebView == null) {
            mURLToLoad = url;
        } else {
            syncJavascriptInterface(url);
            mWebView.loadUrl(url);
        }
    }

    // ------------------------------------------------------------------------
    public boolean goBack() {
        if(mWebView != null && mWebView.canGoBack()) {
            shouldEnableZoom(mWebView.getUrl(), false); // URL doesn't change until we're out of this method
            mWebView.goBack();
            return true;
        } else {
            return false;
        }
    }

    public void launchGameFromIntent(String placeID)
    {
        String gameDetailsUrl = RobloxSettings.baseUrl() + "--place?id=" + placeID;
        String placeLaunchUrl = RobloxSettings.baseUrl() + "games/start?placeid=" + placeID;
        if (mWebView != null) mWebViewClientEmbedded.shouldOverrideUrlLoading(mWebView, placeLaunchUrl);
    }

    public void setDefaultUrl(String def) {
        mDefaultUrl = def;
    }

    public void loadDefaultUrl() {
        if (mWebView != null && mDefaultUrl != null)
            mWebView.loadUrl(mDefaultUrl);
    }

    // Used so we know whether we're closing the Robux or BC dialog
    public void onDismiss(DialogInterface dialog) {
        super.onDismiss(dialog);
        if (!SessionManager.getInstance().getIsLoggedIn())
        {
            if (isBCDialog || isRobuxDialog || isCaptchaDialog)
                RbxAnalytics.fireButtonClick(getDialogContext(), "close");
        }
    }

    private String getDialogContext() {
        if (isBCDialog)
            return "buildersClub";
        else if (isRobuxDialog)
            return "robux";
        else if (isCaptchaDialog)
            return "captcha";

        return "undefinedWebContext";
    }

    @Override
    public void onSaveInstanceState(Bundle outState) {

    }

    public WebviewInterface getJavascriptInterface() { return mWebviewInterface; }
}

class WebviewInterface {
    ActivityNativeMain mActivityRef = null;
    boolean isFirstLaunch = true;
    private String TAG = "WebviewInterface";
    private boolean useCompat = false;
    private WebView mWebViewRef = null;

    WebviewInterface(Activity act, boolean compat, WebView webview) {
        mWebViewRef = webview;
        useCompat = compat;
        try {
            mActivityRef = (ActivityNativeMain)act;
        }
        catch (ClassCastException cce)
        {
            Log.e(TAG, "Tried to cast activity to wrong type.");
        }

        if (RobloxSettings.eventsData == null)
        {
            // This is a fall back in case the events data fails to load before we open this page
            // The first attempted load is in ActivityStart - this is probably only needed on test sites,
            // but it's a good back up to have
            RbxHttpGetRequest eventsReq = new RbxHttpGetRequest(RobloxSettings.eventsUrl(), new OnRbxHttpRequestFinished() {
                @Override
                public void onFinished(HttpResponse response) {
                    if (!response.responseBodyAsString().isEmpty())
                    {
                        try
                        {
                            String nResponse = "{\"Data\":" + response.responseBodyAsString() + "}"; // returned as a JSONArray, need to wrap
                            // it in an object so we can attempt to parse
                            JSONObject j = new JSONObject(nResponse);
                            if (j != null)
                            {
                                RobloxSettings.eventsData = j.toString();
                                // The events payload comes from the network. Round-tripping
                                // it through JSONArray/JSONObject.quote guarantees the
                                // javascript: URL contains data literals, not executable
                                // code (previously a crafted response could inject JS).
                                String eventsLiteral = new JSONArray(
                                        stripPadding(RobloxSettings.eventsData)).toString();
                                mWebViewRef.loadUrl("javascript:parseEvents(" +
                                        JSONObject.quote(RobloxSettings.baseUrlWWW()) + ", " +
                                        eventsLiteral + ", " + RobloxSettings.isPhone() + ", " +
                                        useCompat + ");");
                            }
                        }
                        catch (Exception e)
                        {
                            Log.i("EventsRequest", e.toString());
                            RobloxSettings.eventsData = null;
                        }
                    }
                }
            });
            eventsReq.execute();
        }
    }


    @JavascriptInterface
    public void LogMessage(String msg) {
    }

    @JavascriptInterface
    public String getInitSettings() {
        JSONObject json = new JSONObject();
        try {
            json.put("baseUrl", RobloxSettings.baseUrlWWW());
            json.put("isFirstLaunch", isFirstLaunch);
            json.put("isMobile", RobloxSettings.isPhone());
            json.put("profileUrl", RobloxSettings.profileUrl());
            json.put("characterUrl", RobloxSettings.characterUrl());
            json.put("inventoryUrl", RobloxSettings.inventoryUrl());
            json.put("tradeUrl", RobloxSettings.tradeUrl());
            json.put("groupsUrl", RobloxSettings.groupsUrl());
            json.put("forumUrl", RobloxSettings.forumUrl());
            json.put("blogUrl", RobloxSettings.blogUrl());
            json.put("helpUrl", RobloxSettings.helpUrl());
            json.put("settingsUrl", RobloxSettings.settingsUrl());
            json.put("catalogUrl", RobloxSettings.catalogUrl());
            json.put("reloadMore", RobloxSettings.dontReloadMorePage);
            json.put("isEmailNotificationEnabled", (RobloxSettings.isEmailNotificationEnabled() && RobloxSettings.getUserEmail().isEmpty())
                    || (RobloxSettings.isPasswordNotificationEnabled() && !RobloxSettings.userHasPassword));
            json.put("useCompatibility", useCompat);
            if (RobloxSettings.eventsData != null)
            {
                json.put("eventsData", stripPadding(RobloxSettings.eventsData));
            }
        }
        catch (Exception e)
        {

        }
        if (isFirstLaunch) isFirstLaunch = false;
        if (RobloxSettings.dontReloadMorePage) RobloxSettings.dontReloadMorePage = false;

        return json.toString();
    }

    private String stripPadding(String json)
    {
        // eventsData is stored as {"Data":[...]}. Be defensive: an unexpected
        // shape used to throw StringIndexOutOfBoundsException and could feed
        // arbitrary text into a javascript: URL.
        if (json == null || json.length() < 10 || !json.startsWith("{\"Data\":")
                || !json.endsWith("}"))
        {
            return "[]";
        }
        return json.substring(8, json.length() - 1);
    }

    @JavascriptInterface
    public void transitionToColor(final String newHeader, String c)
    {
        Handler mainThread = new Handler(Looper.getMainLooper());
        Integer color = mActivityRef.getResources().getColor(R.color.black);

        if (c.equals("blue"))
            color = mActivityRef.getResources().getColor(R.color.RbxBlue1);
        else if (c.equals("orange"))
            color = mActivityRef.getResources().getColor(R.color.RbxOrange);
        else if (c.equals("green"))
            color = mActivityRef.getResources().getColor(R.color.RbxGreen1);
        else if (c.equals("purple"))
            color = mActivityRef.getResources().getColor(android.R.color.holo_purple);

        final Integer finalColor = new Integer(color);
        mainThread.postDelayed(new Runnable() {
            @Override
            public void run() {
                mActivityRef.startNewTransition(finalColor);
                mActivityRef.updateMoreProperties(newHeader, finalColor);

                // The pageName comes from the interface.transitionToColor calls in main.js
                mActivityRef.latestMorePage = "tab" + newHeader;
                RbxAnalytics.fireButtonClick("tabMore", newHeader.toLowerCase());
            }
        }, 400);
    }

    @JavascriptInterface
    public void showSettingsDialog()
    {
        Handler mainThread = new Handler(Looper.getMainLooper());
        mainThread.post(new Runnable() {
            @Override
            public void run() {
                mActivityRef.showSettingsDialog();
            }
        });
    }

    @JavascriptInterface
    public void fireScreenLoaded() {
        Handler mainThread = new Handler(Looper.getMainLooper());

        mainThread.post(new Runnable() {
            @Override
            public void run() {
                mActivityRef.latestMorePage = "tabMore";
                RbxAnalytics.fireScreenLoaded("more");
            }
        });
    }

    public void clearSettingsNotification() {
        mWebViewRef.loadUrl("javascript:clearSettingsNotification();");
    }
}