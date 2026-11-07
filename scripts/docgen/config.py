"""
Configuration and constants for R2K16 Codebase Documentation Generator.
"""
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
WEBSITE_DIR = os.path.join(REPO_ROOT, 'website')
DOCS_DIR = os.path.join(WEBSITE_DIR, 'docs')
CODEBASE_DOCS_DIR = os.path.join(DOCS_DIR, 'codebase')

# Modules to scan
CORE_MODULES = [
    'Base',
    'App',
    'Network',
    'Rendering',
    'ClientShared',
    'ClientBase',
    'CSG',
    'WindowsClient',
    'Win',
    'RobloxStudio',
    'RCCService',
    'XboxClient',
    'Roblox.RccServiceArbiter',
    'RbxTestHooks',
    'CoreScriptConverter2',
]

TEST_MODULES = [
    'App.UnitTest',
    'App.UnitTest.Lib',
    'Base.UnitTest',
    'Base.UnitTest.Lib',
    'RobloxTest',
    'Roblox.Test',
    'RCCService.Test',
    'tests',
]

# Third-party / vendored directories to ignore when extracting core engine functions
VENDOR_DIRS = {
    'Library',
    'boostlibs',
    'Lua-5.1.4',
    'lz4',
    'raknet',
    'sgCore',
    'rapidjson',
    'LibOVR',
    'OpenVR',
    'VrApi',
    'node_modules',
    '.git',
    'build',
    'dist',
    'website',
}

SOURCE_EXTENSIONS = {'.cpp', '.c', '.h', '.hpp', '.cs', '.mm', '.m', '.py'}
TEST_EXTENSIONS = {'.cpp', '.h', '.cs', '.py'}

SUBSYSTEM_RULES = [
    ('Base', 'Base Foundations'),
    ('v8datamodel', 'App - DataModel & Hierarchy'),
    ('v8tree', 'App - Instance Tree'),
    ('v8world', 'App - World Simulation & Physics'),
    ('v8kernel', 'App - World Simulation & Physics'),
    ('solver', 'App - Solvers & Humanoids'),
    ('humanoid', 'App - Solvers & Humanoids'),
    ('script', 'App - Scripting & Lua VM'),
    ('reflection', 'App - Reflection System'),
    ('v8xml', 'App - Serialization & XML'),
    ('voxel2', 'App - Voxel Terrain Engines'),
    ('voxel', 'App - Voxel Terrain Engines'),
    ('tool', 'App - Tools & User Input'),
    ('gui', 'App - Tools & User Input'),
    ('security', 'App - Security & Validation'),
    ('util', 'App - Utilities & Math'),
    ('App', 'App - Engine Core'),
    ('Network', 'Network & Replication'),
    ('Rendering', 'Rendering Pipeline'),
    ('ClientShared', 'Client Shared Subsystems'),
    ('ClientBase', 'Client Base Configuration'),
    ('CSG', 'CSG Geometric Kernel'),
    ('WindowsClient', 'Windows Client & Win Launcher'),
    ('Win', 'Windows Client & Win Launcher'),
    ('RobloxStudio', 'Roblox Studio IDE'),
    ('RCCService', 'RCCService Game Server'),
    ('XboxClient', 'Xbox Client Subsystems'),
    ('Roblox.RccServiceArbiter', 'RCCService Game Server'),
    ('RbxTestHooks', 'Tooling & Test Hooks'),
    ('CoreScriptConverter2', 'Tooling & Test Hooks'),
]
