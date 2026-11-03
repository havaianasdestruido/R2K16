#ifndef _ROLBOX_ADAPTER_H_
#define _ROLBOX_ADAPTER_H_

/* Every char* output parameter below (retMessage, cbufHost, value, ...) must
 * point to a buffer of at least this many bytes. The adapter used to assume
 * "bufLen == 0 means the caller allocated enough" and copy a COM BSTR of
 * arbitrary length into it, which is a stack/heap overflow. */
#define ROBLOX_ADAPTER_OUTPUT_BUFFER_SIZE 2048

void StartCom(void);
void StopCom(void);
bool isComStarted(void);

ILauncher * GetIRobloxLauncherInstance(void);

int RobloxAdapterHelloWorld(ILauncher *iIRobloxLauncher);
int RobloxAdapterHello(ILauncher *iIRobloxLauncher,char *retMessage);
int RobloxAdapterStartGame(ILauncher *iIRobloxLauncher,char *cbufAuth, char *cbufScript );
int RobloxAdapterPreStartGame(ILauncher *iIRobloxLauncher);
int RobloxAdapterGet_InstallHost(ILauncher *iIRobloxLauncher,char *cbufHost);
int RobloxAdapterGet_Version(ILauncher *iIRobloxLauncher,char *cbufHost);
int RobloxAdapterUpdate(ILauncher *iIRobloxLauncher);
int RobloxAdapterPut_AuthenticationTicket(ILauncher *iIRobloxLauncher,char *cbufTicket );
int RobloxAdapterGet_IsGameStarted(ILauncher *iIRobloxLauncher, bool *isStarted);
int RobloxAdapterGet_SetSilentModeEnabled(ILauncher *iIRobloxLauncher, bool silendMode);
int RobloxAdapterGet_UnhideApp(ILauncher *iIRobloxLauncher);
int RobloxAdapterBringAppToFront(ILauncher *iIRobloxLauncher);
int RobloxAdapterResetLaunchState(ILauncher *iIRobloxLauncher);
int RobloxAdapterSetEditMode(ILauncher *iIRobloxLauncher);
int RobloxAdapterGet_SetStartInHiddenMode(ILauncher *iIRobloxLauncher, bool hiddenMode);
int RobloxAdapterGet_IsUpToDate(ILauncher *iIRobloxLauncher, bool *isUpToDate);
int RobloxAdapterGetKeyValue(ILauncher *iIRobloxLauncher, char *key, char *value);
int RobloxAdapterSetKeyValue(ILauncher *iIRobloxLauncher, char *key, char *value);
int RobloxAdapterDeleteKeyValue(ILauncher *iIRobloxLauncher, char *key);

#endif

