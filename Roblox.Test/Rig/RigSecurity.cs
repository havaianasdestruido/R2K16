using System;
using System.IO;
using System.Net;
using System.Reflection;
using System.ServiceModel;
using System.ServiceModel.Channels;
using System.ServiceModel.Description;
using System.ServiceModel.Dispatcher;

namespace Roblox.Test
{
    /// <summary>
    /// Security boundary for the distributed test rig.
    ///
    /// The WCF service accepts arbitrary strings (paths, executable names, test
    /// names, machine names) from the network and used to feed them directly into
    /// Process.Start / AppDomain assembly loading / file paths / a SQL string.
    /// Every one of those inputs is validated here, and the service is not
    /// world-callable: set ROBLOX_TEST_RIG_TOKEN to a shared secret to allow
    /// remote callers, otherwise only loopback callers are accepted.
    ///
    /// Targets .NET 3.5 / C# 3.0 (see Roblox.Test.csproj).
    /// </summary>
    internal static class RigSecurity
    {
        internal const string AllowedBinDirVariable = "ROBLOX_TEST_RIG_BIN_DIR";
        internal const string AuthTokenVariable = "ROBLOX_TEST_RIG_TOKEN";
        internal const string AuthHeaderName = "X-Roblox-Test-Token";

        private const int MaxStringLength = 1024;

        private static string AllowedRoot
        {
            get
            {
                string configured = Environment.GetEnvironmentVariable(AllowedBinDirVariable);
                if (!String.IsNullOrEmpty(configured))
                    return Path.GetFullPath(configured);

                Assembly assembly = Assembly.GetEntryAssembly() ?? Assembly.GetExecutingAssembly();
                return Path.GetDirectoryName(Path.GetFullPath(assembly.Location));
            }
        }

        private static bool IsUnderRoot(string candidate, string root)
        {
            string rootWithSeparator = root.TrimEnd(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar)
                + Path.DirectorySeparatorChar;
            return candidate.Equals(root, StringComparison.OrdinalIgnoreCase)
                || candidate.StartsWith(rootWithSeparator, StringComparison.OrdinalIgnoreCase);
        }

        private static void CheckLength(string value, string name)
        {
            if (value != null && value.Length > MaxStringLength)
                throw new ArgumentException(name + " is too long");
        }

        /// <summary>Validates and normalizes an assembly deployment directory.</summary>
        internal static string ValidateBinRoot(string binroot)
        {
            CheckLength(binroot, "binroot");
            string root = AllowedRoot;
            string candidate;
            if (String.IsNullOrEmpty(binroot))
            {
                candidate = root;
            }
            else
            {
                if (!Path.IsPathRooted(binroot))
                    throw new ArgumentException("binroot must be an absolute path");
                candidate = Path.GetFullPath(binroot);
            }
            if (!IsUnderRoot(candidate, root))
                throw new ArgumentException("binroot is outside the allowed test directory");
            return candidate;
        }

        /// <summary>Only executables inside the allowed test directory may be launched.</summary>
        internal static string ValidateExecutable(string filename)
        {
            CheckLength(filename, "filename");
            if (String.IsNullOrEmpty(filename) || !Path.IsPathRooted(filename))
                throw new ArgumentException("filename must be an absolute path");

            string full = Path.GetFullPath(filename);
            if (!IsUnderRoot(full, AllowedRoot))
                throw new ArgumentException("executable is outside the allowed test directory");
            if (full.IndexOf("..", StringComparison.Ordinal) >= 0)
                throw new ArgumentException("executable path contains '..'");
            if (!File.Exists(full))
                throw new ArgumentException("executable does not exist");

            string extension = Path.GetExtension(full);
            if (!extension.Equals(".exe", StringComparison.OrdinalIgnoreCase))
                throw new ArgumentException("only .exe executables may be launched");
            return full;
        }

        /// <summary>Arguments are passed without a shell; reject control characters anyway.</summary>
        internal static string ValidateArguments(string args)
        {
            CheckLength(args, "args");
            if (String.IsNullOrEmpty(args)) return String.Empty;
            foreach (char c in args)
            {
                if (Char.IsControl(c))
                    throw new ArgumentException("arguments contain a control character");
            }
            return args;
        }

        /// <summary>Test names and output file names must be plain, single-segment names.</summary>
        internal static string ValidateName(string value, string fieldName)
        {
            CheckLength(value, fieldName);
            if (String.IsNullOrEmpty(value))
                throw new ArgumentException(fieldName + " is empty");
            if (value.IndexOfAny(new char[] { '/', '\\', ':', '*', '?', '"', '<', '>', '|' }) >= 0
                || value.Contains(".."))
                throw new ArgumentException(fieldName + " is not a plain name");
            foreach (char c in value)
            {
                if (Char.IsControl(c))
                    throw new ArgumentException(fieldName + " contains a control character");
            }
            return value;
        }

        /// <summary>Machine names are interpolated into an http:// URL; reject URL syntax.</summary>
        internal static string ValidateMachineName(string machineName)
        {
            CheckLength(machineName, "machine name");
            if (String.IsNullOrEmpty(machineName))
                throw new ArgumentException("machine name is empty");
            if (machineName.IndexOfAny(new char[] { '/', '\\', ':', '@', '?', '#', '&' }) >= 0)
                throw new ArgumentException("machine name contains URL syntax");
            if (Uri.CheckHostName(machineName) == UriHostNameType.Unknown)
                throw new ArgumentException("machine name is not a valid host name");
            return machineName;
        }

        internal static bool ConstantTimeEquals(string a, string b)
        {
            if (a == null || b == null || a.Length != b.Length) return false;
            int difference = 0;
            for (int i = 0; i < a.Length; ++i)
                difference |= a[i] ^ b[i];
            return difference == 0;
        }

        internal static string CurrentToken
        {
            get { return Environment.GetEnvironmentVariable(AuthTokenVariable); }
        }

        /// <summary>
        /// Loopback by default; when a token is configured it must be supplied in
        /// the X-Roblox-Test-Token HTTP header instead.
        /// </summary>
        internal static bool IsCallerAuthorized(OperationContext context)
        {
            if (context == null) return false;

            string token = CurrentToken;
            object rawRequest;
            if (!String.IsNullOrEmpty(token)
                && context.IncomingMessageProperties.TryGetValue(HttpRequestMessageProperty.Name, out rawRequest))
            {
                HttpRequestMessageProperty request = rawRequest as HttpRequestMessageProperty;
                if (request != null)
                    return ConstantTimeEquals(request.Headers[AuthHeaderName], token);
                return false;
            }

            object rawEndpoint;
            if (!context.IncomingMessageProperties.TryGetValue(RemoteEndpointMessageProperty.Name, out rawEndpoint))
                return false;
            RemoteEndpointMessageProperty endpoint = rawEndpoint as RemoteEndpointMessageProperty;
            if (endpoint == null) return false;
            string address = endpoint.Address;
            return address == "127.0.0.1" || address == "::1" || address == "0:0:0:0:0:0:0:1"
                || String.Equals(address, "localhost", StringComparison.OrdinalIgnoreCase);
        }
    }

    /// <summary>WCF host-side authorization guard.</summary>
    internal sealed class RigAuthorizationManager : ServiceAuthorizationManager
    {
        protected override bool CheckAccessCore(OperationContext operationContext)
        {
            return base.CheckAccessCore(operationContext) && RigSecurity.IsCallerAuthorized(operationContext);
        }
    }

    /// <summary>Adds the shared secret to every outgoing client request.</summary>
    internal sealed class RigAuthEndpointBehavior : IEndpointBehavior
    {
        public void AddBindingParameters(ServiceEndpoint endpoint, BindingParameterCollection bindingParameters) { }
        public void ApplyClientBehavior(ServiceEndpoint endpoint, ClientRuntime clientRuntime)
        {
            clientRuntime.MessageInspectors.Add(new RigAuthMessageInspector());
        }
        public void ApplyDispatchBehavior(ServiceEndpoint endpoint, EndpointDispatcher endpointDispatcher) { }
        public void Validate(ServiceEndpoint endpoint) { }
    }

    internal sealed class RigAuthMessageInspector : IClientMessageInspector
    {
        public object BeforeSendRequest(ref Message request, IClientChannel channel)
        {
            string token = RigSecurity.CurrentToken;
            if (String.IsNullOrEmpty(token) || request == null) return null;

            HttpRequestMessageProperty property;
            object existing;
            if (request.Properties.TryGetValue(HttpRequestMessageProperty.Name, out existing))
                property = existing as HttpRequestMessageProperty;
            else
                property = null;

            if (property == null)
            {
                property = new HttpRequestMessageProperty();
                request.Properties[HttpRequestMessageProperty.Name] = property;
            }
            property.Headers[RigSecurity.AuthHeaderName] = token;
            return null;
        }

        public void AfterReceiveReply(ref Message reply, object correlationState) { }
    }
}
