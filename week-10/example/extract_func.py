"""extract_func.py
This Python program extracts functions from other Python scripts.

The functionality is based on parsing abstract syntax tree (AST) and then picking the specified function.

The usage is described in the bottom of this file.
"""
import argparse
import ast
from importlib import util
import os
import sys
import builtins
import logging
from typing import Dict, Optional

StrDict = Dict[str, Optional[str]]

__version__ = "0.0.0"

class EArgs:
    input_file: str
    func_name: list[str]
    output_file: str
    profiler: bool
    verbose: int
    version: bool

def locateModuleSource(ModuleName: str, PBasePath: str) -> str | None:
    """
    Locate the source file of a module.
    """
    logging.debug("Locating module source for '{}' in '{}'".format(
        ModuleName, PBasePath
        ))
    if not ModuleName or not isinstance(ModuleName, str):
        logging.error("Invalid ModuleName: '{}'".format(ModuleName))
        return None
    elif ModuleName in sys.builtin_module_names: # Check if the module is built-in
        logging.debug("Module '{}' is a built-in module.".format(ModuleName))
        return None
    # Attempt to find the module in the base path
    ModulePath = os.path.join(
        PBasePath, "{}.py".format(ModuleName.replace('.', os.sep))
        )
    logging.debug("Trying ModulePath: '{}'".format(ModulePath))
    if os.path.exists(ModulePath):
        logging.debug("Module found at '{}'".format(ModulePath))
        return ModulePath
    # Try adding the base path to sys.path and using importlib
    if PBasePath not in sys.path:
        sys.path.insert(0, PBasePath)
        logging.debug("Added '{}' to sys.path".format(PBasePath))
    try:
        spec = util.find_spec(ModuleName)
        if spec and spec.origin and spec.origin.endswith(".py"):
            logging.debug("Found module '{}' at '{}'".format(
                ModuleName, spec.origin
                ))
            return spec.origin
        else:
            logging.debug("No origin found for module '{}'".format(
                ModuleName
                ))
    except Exception as Err:
        logging.error("Error finding spec for module '{}': {}".format(
            ModuleName, Err
            ))
    return None

def collectImports(PTree: ast.Module) -> StrDict:
    """
    Collects import statements and builds a mapping of aliases to module names.
    """
    Imports: StrDict = {}
    for Node in PTree.body:
        if isinstance(Node, ast.ImportFrom):
            ModuleName = Node.module
            for Alias in Node.names:
                AliasName = Alias.asname or Alias.name
                # For 'from module import func as alias_name'
                Imports[AliasName] = ModuleName
        elif isinstance(Node, ast.Import):
            for Alias in Node.names:
                AliasName = Alias.asname or Alias.name
                ModuleName = Alias.name
                # For 'import module_name as alias_name'
                Imports[AliasName] = ModuleName
    return Imports

def findFuncWithDeps(
        PTree: ast.Module,
        PSourceLines: list[str],
        PFuncName: str,
        PExtracted: set = None,
        PProfiler: bool = False,
        PBasePath: str = ".",
        ) -> list[str]:
    logging.debug(f"Searching for function '{PFuncName}'")
    if PExtracted is None:
        PExtracted = set()
    if PFuncName in PExtracted:
        return []
    ExtractedCodeLines: list[str] = []
    Imports = collectImports(PTree)
    FuncFound = False
    for Node in PTree.body:
        if isinstance(Node, ast.FunctionDef) and Node.name == PFuncName:
            FuncFound = True
            PExtracted.add(PFuncName)  # Function found
            StartLine = Node.lineno - 1
            EndLine = Node.end_lineno
            if PProfiler:
                ExtractedCodeLines.append("@profile")
            ExtractedCodeLines.extend(PSourceLines[StartLine:EndLine])
            for SubNode in ast.walk(Node):
                if isinstance(SubNode, ast.Call):
                    CalledFunc = None
                    if isinstance(SubNode.func, ast.Name):
                        CalledFunc = SubNode.func.id
                        if CalledFunc in dir(builtins):
                            continue  # Skip built-in functions
                        if CalledFunc not in PExtracted:
                            # Check if the function is imported directly
                            ModuleName = Imports.get(CalledFunc)
                            if ModuleName: # Function is imported directly
                                ExtractedCodeLines.extend(
                                    findFuncInModule(
                                        ModuleName,
                                        CalledFunc,
                                        PExtracted,
                                        PProfiler=PProfiler,
                                        PBasePath=PBasePath
                                    )
                                )
                            else: # Search locally
                                ExtractedCodeLines.extend(
                                    findFuncWithDeps(
                                        PTree,
                                        PSourceLines,
                                        CalledFunc,
                                        PExtracted,
                                        PProfiler=PProfiler,
                                        PBasePath=PBasePath,
                                    )
                                )
                    elif isinstance(SubNode.func, ast.Attribute):
                        if isinstance(SubNode.func.value, ast.Name):
                            ModuleAlias = SubNode.func.value.id
                            CalledFunc = SubNode.func.attr
                            if CalledFunc in dir(builtins):
                                continue  # Skip built-in functions
                            ModuleName = Imports.get(ModuleAlias)
                            if ModuleName:
                                # Function is accessed via module alias
                                ExtractedCodeLines.extend(
                                    findFuncInModule(
                                        ModuleName,
                                        CalledFunc,
                                        PExtracted,
                                        PProfiler=PProfiler,
                                        PBasePath=PBasePath
                                    )
                                )
            break  # Function found, exit the loop
    if not FuncFound: # Search other imported modules
        for Alias, ModuleName in Imports.items():
            # Avoid re-searching in modules already processed
            if (ModuleName, PFuncName) in PExtracted:
                continue
            PExtracted.add((ModuleName, PFuncName))
            ExtractedCodeLines.extend(
                findFuncInModule(
                    ModuleName,
                    PFuncName,
                    PExtracted,
                    PProfiler=PProfiler,
                    PBasePath=PBasePath
                )
            )
            if PFuncName in PExtracted: # Found in the imported module
                return ExtractedCodeLines
        logging.debug("Function '{}' not found anywhere.".format(
            PFuncName
            ))
        return []
    return ExtractedCodeLines

def findFuncInModule(
        ModuleName: str,
        PFuncName: str,
        PExtracted: set,
        PProfiler: bool,
        PBasePath: str
        ) -> list[str]:
    """
    Search for a function in a specific module.
    """
    logging.debug("Searching for function '{}' in module '{}'".format(
        PFuncName,
        ModuleName
        ))
    ModuleSource = locateModuleSource(ModuleName, PBasePath)
    if ModuleSource:
        with open(ModuleSource, "r") as f:
            ExternalSourceCode = f.read()
        ExternalTree = ast.parse(ExternalSourceCode)
        ExternalLines = ExternalSourceCode.splitlines()
        # Recursively extract function from the external module
        return findFuncWithDeps(
            ExternalTree,
            ExternalLines,
            PFuncName,
            PExtracted,
            PProfiler=PProfiler,
            PBasePath=os.path.dirname(ModuleSource),
        )
    else:
        logging.warning(f"Module '{ModuleName}' not found.")
    return []

def extractFuncWDeps(
        PSourceCode: str,
        PFuncName: str,
        PProfiler: bool = False,
        PBasePath: str = '.'
        ) -> str:
    """
    Extract a function and its dependencies from the source code.
    """
    logging.debug(
        "Extracting function '{}' with dependencies in directory '{}'".format(
            PFuncName, PBasePath
        ))
    Tree = ast.parse(PSourceCode)
    SrcLines = PSourceCode.splitlines()
    ExtractedCode = findFuncWithDeps(
        Tree,
        SrcLines,
        PFuncName,
        PProfiler=PProfiler,
        PBasePath=PBasePath
        )
    return "\n".join(ExtractedCode) + '\n'

def findFuncInModule(
        ModuleName: str,
        PFuncName: str,
        PExtracted: set,
        PProfiler: bool,
        PBasePath: str
        ) -> list[str]:
    """
    Search for a function in a specific module.
    """
    logging.debug(f"Searching for function '{PFuncName}'")
    ModuleSource = locateModuleSource(ModuleName, PBasePath)
    if ModuleSource:
        with open(ModuleSource, "r") as f:
            ExternalSourceCode = f.read()
        ExternalTree = ast.parse(ExternalSourceCode)
        ExternalLines = ExternalSourceCode.splitlines()
        return findFuncWithDeps(
            ExternalTree,
            ExternalLines,
            PFuncName,
            PExtracted,
            PProfiler=PProfiler,
            PBasePath=os.path.dirname(ModuleSource),
        )
    return []

def readFile(PFilepath: str) -> str:
    try:
        Filehandle = open(PFilepath, 'r', encoding="UTF-8")
        Content = Filehandle.read()
        Filehandle.close()
    except Exception:
        print("Couldn't read source file '{}'".format(PFilepath))
        sys.exit(1)
    return Content

def writeFile(PFilepath: str, PContent: str) -> None:
    try:
        Filehandle = open(PFilepath, 'w', encoding="UTF-8")
        Filehandle.write(PContent)
        Filehandle.close()
    except Exception:
        print("Couldn't write a file.")
        sys.exit(1)
    return None

def handleArgs(pArgs: EArgs) -> None:
    if pArgs.version:
        print(__version__)
        return None
    SourceCode = readFile(pArgs.input_file)
    BasePath = os.path.dirname(os.path.abspath(pArgs.input_file))
    FuncCodes = []
    for FuncName in pArgs.func_name:
        ExtractedCode = extractFuncWDeps(
            SourceCode,
            FuncName,
            pArgs.profiler,
            PBasePath=BasePath
        )
        if ExtractedCode.strip():
            FuncCodes.append(ExtractedCode)
            if pArgs.verbose > 0:
                print(f"#### Function {FuncName} ####")
                print(ExtractedCode)
                print(f"#### Function {FuncName} ####")
        else:
            print(
                "Warning: Function '{}' not found.".format(FuncName),
                file=sys.stderr
                )
    FuncCode = '\n\n'.join(FuncCodes)
    if not FuncCode.strip():
        ErrorMsg = "Couldn't find the following functions in '{}':\n".format(
            pArgs.input_file
        )
        for FuncName in pArgs.func_name:
            ErrorMsg += f" - {FuncName}\n"
        print(ErrorMsg, file=sys.stderr)
    else:
        writeFile(pArgs.output_file, FuncCode)
    return None

def main() -> None:
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser(
        description="""
        Extract a Python function by name from a source file.

        Subtracts only pure functions and their dependencies.
        It won't extract any global variables or other things outside the
        function's scope.
        """
    )
    parser.add_argument(
        '-v',
        '--version',
        action='store_true'
        )
    args, _ = parser.parse_known_args()
    if args.version:
        print(__version__)
        sys.exit(1)
    parser.add_argument(
        '-i',
        '--input-file',
        required=True,
        help='Path to the source Python file.'
        )
    parser.add_argument(
        '-f',
        '--func-name',
        required=True,
        nargs='+',
        help='Name(s) of the functions to extract.'
        )
    parser.add_argument(
        '-o',
        '--output-file',
        required=True,
        help='Path to the destination Python file.'
        )
    parser.add_argument(
        '-p',
        '--profiler',
        action='store_true',
        help='Add profiler decorator to the subtracted functions'
        )
    parser.add_argument(
        '-V',
        '--verbose',
        action='count',
        default=0,
        help="Verbosity level"
        )
    args = parser.parse_args()
    handleArgs(args)
    return None

main()

"""
Commands to use:

# Subtract existing quickSort function
python extract_func.py -i A10_E1.py -f quickSort -o codeA10_E1.py --verbose
# Subtract non-existing quick_sort function
python extract_func.py -i A10_E1.py -f quick_sort -o codeA10_E1.py -V
# Help message
python extract_func.py --help
# Version
python extract_func.py --version
"""