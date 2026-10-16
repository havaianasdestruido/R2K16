# Repository audit report — 2026-10-16

**Repository:** `havaianasdestruido/R2K16`
**Audited revision:** `60417a2b6a64fa9c5e4dbe3a2c80ac34708362bc` (`main` base; checkout branch `arena/49baf2ae-r2k16`)
**Publication status:** GitHub Issues are disabled (`hasIssuesEnabled=false`), and Discussions are disabled. **No GitHub Issues were created.** This file contains issue-ready drafts for the confirmed, actionable findings; none has an issue number or URL.

No implementation source was changed. Website dependencies/build output created during verification are ignored by Git. Secret values and machine-specific absolute paths are intentionally omitted/redacted throughout this report.

## Issue-ready drafts

### 1. Remove and rotate the committed Android release-signing material

- **Severity:** High; potentially critical if this is still the key used to sign distributed releases.
- **Subsystem:** Android release signing / credential management.
- **Evidence:** `Android/NativeShell/build.gradle:70–76` declares the `packageRelease` signing configuration with inline store/key credentials and points to `../robloxAndroidPK_DO_NOT_DELETE`. `build.gradle:166–169` explicitly assigns that configuration to the `release` build type. The referenced tracked file is 1,407 bytes and begins with the JKS keystore magic bytes. Credential values are deliberately not reproduced here.
- **Root cause:** A private signing key and its credentials are stored in a public source repository rather than injected from a protected signing environment.
- **Impact:** Anyone who can retrieve the repository can attempt to use the key material to sign releases. If it is trusted by an existing distribution, compromise may enable impersonation or malicious updates; its production status is not established.
- **Recommended fix:** Treat the material as disclosed. Confirm whether it is or was used for distributed releases and rotate/retire it under the relevant Android distribution process if active. Remove the file and inline credentials from the working tree; load release credentials from a protected CI secret or ignored local file. Removing the current copy alone does not make an already-public key private again.
- **Acceptance criteria:** No signing secret or keystore is tracked; release signing uses protected, injected credentials and fails safely when they are absent; the owner documents the old key’s status and rotates it if active; a release build is verified with the replacement configuration.
- **Verification limits:** The release-task association is confirmed. Java/`keytool` is unavailable here, so the keystore’s password, alias validity, certificate, and actual production use were not verified. No key values are included in this report.

### 2. Revoke the public Crashlytics/Fabric API secret

- **Severity:** High.
- **Subsystem:** Android Crashlytics / credential management.
- **Evidence:** `Android/NativeShell/crashlytics.properties:1,3` is tracked and contains a non-empty `apiSecret` entry. Its own comment says the value validates the application and should not be made public. `Android/NativeShell/build.gradle:7,11` configures the Fabric Gradle plugin. The secret value is redacted.
- **Root cause:** A provider API secret was committed in a public repository despite the file’s explicit warning.
- **Impact:** If the credential is still valid, another party may be able to perform operations permitted by that Crashlytics/Fabric credential. Its current validity and exact permissions are not known.
- **Recommended fix:** Revoke/rotate the existing secret in the provider account, remove it from tracked files, and inject a replacement only into authorized build/upload jobs. Keep a value-free example/template if the build needs local configuration.
- **Acceptance criteria:** The exposed credential is revoked or rotated; no active secret remains in the current tracked tree; builds obtain the replacement from protected configuration; secret scanning does not find the old value in the current source.
- **Verification limits:** The provider account could not be inspected, so validity and capabilities were not tested. The secret value is intentionally omitted.

### 3. Stop writing Android authentication material to logcat

- **Severity:** High (sensitive reusable credentials are logged; access to device logs is environment-dependent).
- **Subsystem:** Android authentication / HTTP diagnostics.
- **Evidence:** `SessionManager.java:551–557,582–587,682–685` URL-encodes the entered password and places it in login POST bodies. URL encoding is reversible, not encryption. `HttpAgent.java:163–169` logs the entire `post` string when an `IOException` occurs; a failed response can enter this path when `getInputStream()` throws. Separately, `WebkitCookieManagerProxy.java:73–74` passes a `.ROBLOSECURITY` `Set-Cookie` header to `getAndSetLatestCookieExpiration`, and line 120 logs the complete header value. `SocialManager.java:145–150` also logs the UID signature used in the subsequent social-login request.
- **Root cause:** Diagnostic logging prints secret-bearing request bodies, cookie headers, and authentication signatures without redaction.
- **Impact:** Any ADB/debug session, privileged log reader, diagnostic collector, or bug report that captures these logs can expose account passwords, reusable session cookies, or social-auth material.
- **Recommended fix:** Remove request-body and cookie-value logging. Log only safe metadata (operation, status, elapsed time); redact authentication fields and signatures before any diagnostics. Do not log a full `Set-Cookie` header.
- **Acceptance criteria:** Tests or instrumentation using synthetic credentials exercise failed login, cookie receipt, and social-login paths and confirm no password, `.ROBLOSECURITY` value, or UID signature appears in log output; useful non-sensitive status diagnostics remain.
- **Verification limits:** Source-level data flow is confirmed. No Android runtime/logcat environment is installed, so the device-level reproduction was not run. Access to logs varies by Android version and device configuration.

### 4. Keep Android Influx credentials out of request URLs

- **Severity:** Medium; conditional on telemetry being configured and sent.
- **Subsystem:** Android telemetry / InfluxDB authentication.
- **Evidence:** `AndroidAppSettings.java:68–73` reads `InfluxUrl`, `InfluxUser`, and `InfluxPassword` from app settings. `InfluxBuilderV2.java:95–108` appends the username and password as `u=`/`p=` query parameters and sends the URL in an HTTP POST. `HttpAgent.java:129–132` logs the full URL for every status other than 200. The Influx code’s commented response check at `InfluxBuilderV2.java:115–116` treats 204 as the expected write result, which is also logged by that generic `status != 200` condition.
- **Root cause:** Telemetry credentials are placed in a URI, and the HTTP layer logs complete URIs.
- **Impact:** Credentials can appear in logcat and in request-URI logging at intermediaries or servers; a credential with write access could be misused. The actual credential’s permissions are unknown.
- **Recommended fix:** Use the Influx-supported authorization header or another non-URI credential mechanism, require HTTPS for the configured endpoint, and ensure HTTP diagnostics redact query strings. Do not solve only the log statement while leaving secrets in the request URI.
- **Acceptance criteria:** With telemetry enabled, success (204), error, and network-failure paths contain no username/password in URLs or logs; the configured server accepts the safer auth mechanism and telemetry still works.
- **Verification limits:** The live app-settings payload, endpoint scheme, credential validity, and whether this feature is enabled in a deployed build could not be checked. The source path and log behavior are confirmed.

### 5. Fetch Android remote app settings over HTTPS

- **Severity:** Medium.
- **Subsystem:** Android transport security / remote configuration.
- **Evidence:** `RobloxSettings.java:223` constructs the app-settings URL with the `http://` scheme. `ActivitySplash.java:199–210` invokes `AndroidAppSettings.fetchFromServer` during startup; `AndroidAppSettings.java:21–31` parses the response body and stores the JSON as trusted application settings. `AndroidAppSettings.java:49–85` consumes values including feature flags and telemetry configuration.
- **Root cause:** The app accepts remotely supplied configuration over cleartext HTTP, with no HTTPS-only check or response-integrity validation in this path.
- **Impact:** An on-path attacker can forge or modify the response before the client stores it, changing application behavior and any configuration values returned by the service. Any secrets returned by that endpoint would also lack transport confidentiality.
- **Recommended fix:** Use an HTTPS endpoint, reject cleartext/downgraded redirects, and keep any required fallback secure. Add an assertion/test that the settings URL is HTTPS.
- **Acceptance criteria:** Startup settings requests use HTTPS end to end; a cleartext response is rejected; ordinary settings parsing and startup continue on the secure endpoint.
- **Verification limits:** The legacy backend’s current availability and returned settings were not tested. The source constructs an HTTP URL and consumes the response as configuration; no claim is made about which remote values are currently returned.

### 6. Remove machine-specific Android SDK/NDK paths from the build

- **Severity:** Medium.
- **Subsystem:** Android/RobloxHybrid build configuration.
- **Evidence:** `Android/NativeShell/build.gradle:213–219` invokes an NDK executable using a fixed absolute path and makes that task a dependency of every `JavaCompile` task. Three tracked local configuration files contain absolute SDK/NDK paths: `Android/gradle/local.properties`, `Android/RobloxAndroidTests/local.properties`, and `RobloxHybrid/platforms/android/Hybrid/local.properties`. Their values are intentionally omitted. The hard-coded NDK executable and these absolute paths are absent in this checkout/runtime; `ndk-build` is not on `PATH`.
- **Root cause:** Developer-local SDK/NDK locations are committed or embedded in Gradle rather than resolved from a supported local/CI configuration.
- **Impact:** A clean checkout on another machine or operating system can fail before compiling because Gradle tries to use paths that do not exist there. The unconditional Java compile dependency also couples Java builds to the fixed NDK location.
- **Recommended fix:** Untrack machine-local `local.properties` files and ignore them; provide value-free templates if useful. Resolve the NDK through the Android SDK/NDK configuration or a documented environment variable, and attach native-build prerequisites only to tasks that require them.
- **Acceptance criteria:** A clean checkout builds the documented Android targets after setting standard SDK/NDK configuration, without editing tracked files or installing the NDK at a repository-specific absolute path; no machine-specific `local.properties` remains tracked.
- **Verification limits:** No Java, Gradle runtime, Android SDK, or NDK is available here, so the Android build itself could not be run. The hard-coded task dependency and tracked absolute paths are confirmed.

### 7. Remove the undefined `Log` object target from root CMake

- **Severity:** Medium (blocks root CMake generation).
- **Subsystem:** CMake/native build.
- **Evidence:** `CMakeLists.txt:106` comments out `add_subdirectory(Log)`, but `CMakeLists.txt:146` still includes `$<TARGET_OBJECTS:Log>` in the `roblox` library. No `Log` target definition exists in the repository. The log implementation is already included in the `Base` target (`Base/CMakeLists.txt:98`, `Base/util/Log.cpp`). A local configure/generate using CMake 4.4.4 failed with `Objects of target "Log" referenced but no such target exists`.
- **Root cause:** The top-level object list retained a stale `Log` target reference after the `Log` subdirectory was disabled or the implementation moved into `Base`.
- **Impact:** Root CMake configure/generation fails before a native build can start, even when the intended platform and external dependencies are supplied.
- **Recommended fix:** Remove the stale object reference or define the intended target in one place; avoid compiling `Base/util/Log.cpp` twice. Update the CMake guide to match the actual top-level and nested minimum-version/platform behavior.
- **Acceptance criteria:** Root CMake generation with the documented dependency tree no longer references an undefined target; the resulting native target contains the logging implementation exactly once; the supported configure/build path passes.
- **Verification limits:** The local test used an intentionally empty external contribution directory, so missing Boost/libwww inputs in that test are environment artifacts. The undefined `Log` reference is independent and was reproduced. No full C++ build was run. The docs’ statement that the root file itself requires CMake 2.8 is also inaccurate (the root declares 3.5.0); older nested CMake files are present.

### 8. Make the Microsoft C++ analysis workflow configure a supported build

- **Severity:** Medium (the analysis check does not reach analysis/SARIF upload).
- **Subsystem:** GitHub Actions / MSVC analysis.
- **Evidence:** `.github/workflows/msvc.yml:33–41` runs on `windows-latest` and configures the root CMake project with `cmake -B ...` without supplying `CONTRIB_PATH`. The repository’s CMake guide describes the root CMake path as Unix/Android and directs Windows builds to `Roblox.sln`; it also documents the external contribution path as required. The latest run, [38611652065](https://github.com/havaianasdestruido/R2K16/actions/runs/38611652065), failed at `Configure CMake`; several recent runs fail at that same step.
- **Root cause:** The workflow asks a Windows/MSVC analysis job to configure an incomplete/unsupported root CMake setup and omits its documented external dependency input. The root’s undefined `Log` target is tracked separately in Draft 7 and is another configure blocker.
- **Impact:** The Microsoft analysis action and SARIF upload are skipped, leaving this CI check without usable C++ analysis results.
- **Recommended fix:** Configure a build system supported by the MSVC analysis action (for example, the Windows solution if compatible), or provide a Windows-supported CMake configuration and all required dependencies. Avoid treating the Unix/Android root configure as a working Windows analysis build.
- **Acceptance criteria:** A fresh push/PR reaches the analysis action, produces SARIF, and completes successfully; the workflow’s chosen platform/generator and dependency setup are documented and reproducible.
- **Verification limits:** GitHub’s hosted diagnostic was unavailable; the run API reports only the failed step and a generic exit status. The workflow failure is confirmed, but the precise first Windows-side error was not isolated. This draft intentionally does not duplicate the separate undefined-target issue.

### 9. Fix write permissions before mounting the Docusaurus output into Pages

- **Severity:** Medium (Pages deployment is blocked).
- **Subsystem:** GitHub Pages deployment / workflow filesystem permissions.
- **Evidence:** `.github/workflows/docs-deploy.yml:58–67` builds Jekyll with `actions/jekyll-build-pages@v1` into `./_site`, then a host-runner shell executes `mkdir -p _site/docs` and copies `website/build`. The Jekyll action declares `runs.using: docker` ([action.yml](https://github.com/actions/jekyll-build-pages/blob/v1/action.yml)); its [Dockerfile](https://github.com/actions/jekyll-build-pages/blob/v1/Dockerfile) has no non-root `USER` declaration, so the container’s default root user writes into the shared workspace. The host-runner shell subsequently needs write permission on that output. The latest Pages run, [37129979944](https://github.com/havaianasdestruido/R2K16/actions/runs/37129979944), passed the site builds but failed at `Mount the docs under /docs/`; the deploy job was skipped. A local POSIX permission simulation confirmed that a non-writable build destination rejects `mkdir _site/docs`.
- **Root cause:** Strongly supported container/host ownership mismatch: the Docker action creates `_site` as root, then the host runner attempts to create a child directory without write permission.
- **Impact:** The combined artifact is never uploaded, so the Pages deployment does not run.
- **Recommended fix:** Ensure the next shell step owns/writes `_site` (for example, change ownership to the runner or perform the mount with appropriate permissions), or build Jekyll output as the runner user.
- **Acceptance criteria:** The workflow can create `_site/docs`, copy the Docusaurus build, upload one artifact containing both sites, and complete deployment; verify both the primary page and `/docs/` after deployment.
- **Verification limits:** The hosted step’s exact stderr/permission message could not be retrieved. The failed step and permission model are confirmed; the ownership explanation is the strongly supported cause, not a recovered remote diagnostic. The Docusaurus build itself succeeds locally.

### 10. Upgrade the website dependency tree with npm audit findings

- **Severity:** High (build/development toolchain; not evidence that the deployed static files are vulnerable at runtime).
- **Subsystem:** Website dependencies / supply-chain security.
- **Evidence:** After `npm ci`, `npm audit` reported **49 findings**: 16 critical, 16 high, 15 moderate, and 2 low. The locked direct packages `@docusaurus/core`, `@docusaurus/preset-classic`, and `@docusaurus/theme-mermaid` are all 3.10.2 and are reported critical. `website/package.json` declares these under `dependencies`; `npm audit --omit=dev` therefore reports the same totals. The docs build succeeds. Open PR [#8](https://github.com/havaianasdestruido/R2K16/pull/8) updates `http-cache-semantics` in the website lockfile plus docs tooling dependencies, but does not resolve the broader Docusaurus findings.
- **Root cause:** The website lockfile resolves an outdated vulnerable Docusaurus/transitive dependency tree.
- **Impact:** Vulnerable packages execute in the documentation build/development toolchain; the audit includes critical/high advisories, including build-time or development-server risks. GitHub Pages serves static build output, so no live Node.js runtime exposure was established.
- **Recommended fix:** Upgrade the Docusaurus packages and affected transitive dependencies to supported patched versions, update the lockfile, and review the Docusaurus major-version migration if required. Track the `http-cache-semantics` item in PR #8 rather than duplicating it here.
- **Acceptance criteria:** `npm ci` and `npm run build` pass; `npm audit` has no critical/high findings (or any remaining exception is narrowly documented with an explicit risk rationale); the Pages build/deploy remains successful.
- **Verification limits:** Audit results are from the registry’s current advisory database on 2026-10-16. No forced dependency update was applied. No claim is made that these Node packages are included in the deployed static runtime.

### 11. Make `Events.Slot.emit` safe when a listener unsubscribes during dispatch

- **Severity:** Medium.
- **Subsystem:** RobloxHybrid JavaScript event dispatch.
- **Evidence:** `RobloxHybrid/src/common/events.js:58–66` removes listeners with `splice`, while `emit` at lines 81–87 captures the original `listeners.length` and then indexes the mutable list. I loaded the actual module in Node and registered two listeners; the first unsubscribed itself. `emit` then threw `TypeError: listener is not a function` and the second listener was not called. This is reachable through the built-in `Input` event slots (`RobloxHybrid/src/modules/input.js:16,24`) and the native bridge (`RobloxHybrid/src/common/bridge.js:53–58`; Android dispatch is in `RBHybridWebView.java:206–215`). `RobloxHybrid/build_js.sh` bundles this source for the app.
- **Root cause:** The dispatcher uses a cached listener count while callbacks can mutate the array it is traversing.
- **Impact:** A normal listener lifecycle action can abort event delivery and prevent later subscribers from receiving keyboard/input events.
- **Recommended fix:** Iterate over a stable snapshot or use mutation-safe iteration with explicitly defined behavior for listeners added/removed during dispatch.
- **Acceptance criteria:** Unit tests cover self-unsubscribe, removing a later listener, adding a listener, and the existing `return true` stop-propagation contract; no `TypeError` occurs and remaining listeners follow the documented dispatch semantics. Regenerate the tracked bundle/Android asset through the existing build process.
- **Verification limits:** The JavaScript failure is reproduced directly against source. Native device execution and the Closure Compiler build were not run.

## Deduplication and publication check

- Repository Issues are disabled and no Discussions categories/discussions are available. There are no issue numbers or issue URLs to report.
- PR #8 is the only open PR. Its website changes do not cover the Docusaurus vulnerability set; the `http-cache-semantics` update is explicitly excluded from Draft 10 to avoid duplication.
- PR #4 introduced the current two-site Pages workflow but is merged; no open PR fixes the mount step.
- The CMake `Log` target is drafted once. It also blocks the MSVC configure path, but Draft 8 tracks the separate Windows/platform/dependency setup defect rather than duplicating the target fix.
- The release keystore/passwords and the Crashlytics API secret are separate findings because they are different credentials with different rotation/release processes.
- Android password/cookie/social-auth logging is consolidated into Draft 3 because the shared issue is unredacted sensitive-data logging. The Influx URL is separate (Draft 4) because moving that credential out of the URI is still required even if logging is redacted.
- The CMake documentation’s inaccurate minimum-version/platform wording is included with Draft 7 rather than opened as a standalone documentation ticket.
- OSV-Scanner startup failures are not drafted as a defect because no root cause was confirmed; details are in “Unresolved suspicions.”

## Tests and tools run

- `npm ci` in `website/` — passed (1,390 packages installed).
- `npm run build` in `website/` — passed.
- `npm audit` and `npm audit --omit=dev` in `website/` — both reported 49 findings (16 critical, 16 high, 15 moderate, 2 low); they exit nonzero. `npm audit fix --dry-run` was also reviewed; it was not applied and no dependency fix was made.
- CMake 4.4.4 configure/generate using a deliberately empty temporary contribution directory — failed at generation with the undefined `Log` target. Missing external Boost/libwww inputs from the empty directory are not attributed to the target defect.
- Node.js harness loading `RobloxHybrid/src/common/events.js` — reproduced the listener-unsubscribe `TypeError` and skipped second callback.
- POSIX permission simulation for a non-writable Pages destination — `mkdir _site/docs` failed with `PermissionError`.
- GitHub API/`gh`: reviewed all repository PRs, workflow run/job summaries, PR #8, PR #4, and discussion metadata. Latest Microsoft C++ run failed at `Configure CMake`; latest Pages run failed at the docs mount; latest OSV-Scanner run is `startup_failure` with zero jobs. Recent Semgrep, CodeQL, and Scorecard runs succeeded.
- Android credential/config references were examined with values redacted. No Android/Gradle/NDK build or runtime test was possible.
- `git status` was clean before this report was created. No implementation code was changed.

## Unresolved suspicions and coverage limitations

- OSV-Scanner has repeated `startup_failure` runs with zero jobs, but the referenced upstream reusable workflow files exist and accept the configured `scan-args`; the exact startup cause is unavailable. No issue is drafted without a verified root cause.
- The hosted MSVC and Pages diagnostics could not be retrieved. Their failed steps are confirmed (recent MSVC runs also fail at `Configure CMake`), but the exact Windows-side CMake error and Pages permission stderr remain unavailable.
- The release keystore’s validity and use in an actual distributed production release are unknown. Treat it as compromised if it is active; do not repeat its credentials.
- The Crashlytics secret’s validity/permissions and the current Influx endpoint/configuration are unknown; no credential was tested.
- Android, iOS/Xcode, Windows/MSVC compilation, .NET/MSBuild, Jekyll, and the repository’s native test suites were not run because the required toolchains are unavailable. The merged PR #11 C++ changes were reviewed but remain uncompiled; no defect is asserted from that review. The workspace is shallow, limiting historical review. A broad heuristic secret scan timed out, so this is not a claim that no other secrets exist.
- The GitHub security/code-scanning metadata API returned 403; existing security alerts could not be reviewed through that API. This does not change the confirmed local `npm audit` results.
