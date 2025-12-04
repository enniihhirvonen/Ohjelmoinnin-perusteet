"""test_A10_E1.py
This is a "pytest" file, which can contain any programmatic tests, usually unit and integration tests.

This test suite specificly is being used in CG to test and evaluate functions.

You can run this file if you install pytest library and then see the test results on your local machine.

This file may give insight into the testing procedures that otherwise may not be obvious.
"""
import copy
import hashlib
import importlib
import math
import subprocess
import sys
import tracemalloc
from time import time
from typing import Callable

import pytest

DATASETS = ("A10_D10.txt", "A10_D100.txt", "A10_D1000.txt", "A10_D1024.txt", "A10_D10000.txt", "A10_D100000.txt")
MAIN_CODEFILE = "A10_E1.py"
ALGORITHM_NAME = "quickSort"
EXTRACTED_CODEFILE = "codeA10_E1.py"

def readValues(PFilename: str, PValues: list[int]) -> None:
    PValues.clear()
    try:
        Filehandle = open(PFilename, 'r', encoding="UTF-8")
        while True:
            Line = Filehandle.readline() # Read line and move stream position to next line
            if (len(Line) == 0): # File ends
                break
            elif (Line == '\n'): # Empty line
                continue
            else:
                Row = Line.rstrip('\n') # This right strip removes newline from the right side 
                Value = int(Row) # Convert string to integer
                PValues.append(Value)
        Filehandle.close() # Vapautetaan varatut resurssit takaisin järjestelmälle
    except Exception:
        print("Couldn't read file '{}'.".format(PFilename))
        sys.exit(1) # 1 - virhetilanne
    return None

def sortingErrorMsg(
        ExpectedArr: list[str],
        ActualArr: list[str]
        ) -> str:
    Msg = "\n- Expected order:"
    for Item in ExpectedArr:
        Msg += " " + str(Item)
    Msg += '\n'
    Msg += "- Actual order:"
    for Item in ActualArr:
        Msg += " " + str(Item)
    Msg += '\n'
    return Msg

def hashFile(PFilepath: str) -> str:
    """Generate an MD5 hash for a file."""
    HashFn = hashlib.md5()
    Filehandle = open(PFilepath, 'rb')
    Chunk = Filehandle.read(8192)
    while Chunk:
        HashFn.update(Chunk)
        Chunk = Filehandle.read(8192)
    Filehandle.close()
    FileHash = HashFn.hexdigest()
    return FileHash

def measureTime(PSortAlgorithm: Callable, PArr: list[int]) -> float:
    StartTime = time()
    PSortAlgorithm(PArr)
    EndTime = time()
    ElapsedTime = EndTime - StartTime
    return ElapsedTime

def sortingErrorMsg(
        ExpectedArr: list[str],
        ActualArr: list[str]
        ) -> str:
    Msg = "\n- Expected order:"
    for Item in ExpectedArr:
        Msg += " " + str(Item)
    Msg += '\n'
    Msg += "- Actual order:"
    for Item in ActualArr:
        Msg += " " + str(Item)
    Msg += '\n'
    return Msg

def test_find_quicksort() -> None:
    """Extracts quickSort function from the main code file."""
    result = subprocess.run(
        ["python", "extract_func.py", "-i", MAIN_CODEFILE, "-f", ALGORITHM_NAME, "-o", EXTRACTED_CODEFILE, "-V"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert result.returncode == 0, f"Unexpected exit code: {result.returncode}"
    return None

@pytest.mark.skip(reason="Not part of requirements.")
def test_image_hash_comparison():
    PngExpectedRaw10 = hashFile("Expected_A10_D10_raw.png")
    PngActualRaw10 = hashFile("A10_D10_raw.png")
    print(PngActualRaw10)
    print(PngExpectedRaw10)
    """Test that two image files are identical by hash."""
    assert (PngExpectedRaw10 == PngActualRaw10)
    return None

@pytest.mark.parametrize(
    "PDataset",
    [
        (DATASETS[0]),
        (DATASETS[1]),
        (DATASETS[2]),
    ],
)
def test_sorting(PDataset: str) -> None:
    RawArr = []
    readValues(PDataset, RawArr)
    ActualArr = copy.deepcopy(RawArr)
    ExpectedArr = sorted(RawArr, reverse=False) # ASCending
    print("Testing sorting with {}.".format(ALGORITHM_NAME))
    CodeModule = importlib.import_module(EXTRACTED_CODEFILE.rstrip('.py'))
    getattr(CodeModule, ALGORITHM_NAME)(ActualArr)
    try:
        assert ActualArr == ExpectedArr, "Sorting failed!"
    except AssertionError:
        errMsg = sortingErrorMsg(ExpectedArr, ActualArr)
        pytest.fail(str(errMsg))
    RawArr.clear()
    ActualArr.clear()
    ExpectedArr.clear()
    return None

@pytest.mark.parametrize(
    "PDataset",
    [
        # (DATASETS[0]),
        # (DATASETS[1]),
        (DATASETS[2]),
        # (DATASETS[3]),
        # (DATASETS[4]),
        # (DATASETS[5]),
    ],
)
def test_memory_usage(PDataset: str) -> None:
    print("Testing {} memory usage.".format(ALGORITHM_NAME))
    CodeModule = importlib.import_module(EXTRACTED_CODEFILE.rstrip('.py'))
    ActualArr: list[int] = []
    readValues(PDataset, ActualArr)
    print("Memory before sorting: {1}".format(*tracemalloc.get_traced_memory()))
    tracemalloc.start()
    # ExpectedArr = sorted(RawArr, reverse=False) # ASCending
    getattr(CodeModule, ALGORITHM_NAME)(ActualArr)
    Current, Peak = tracemalloc.get_traced_memory()
    print("Memory after sorting: {1}".format(*tracemalloc.get_traced_memory()))
    tracemalloc.stop()
    BytesPerFrame = 248 # Estimated
    BestScenarioMem = math.log2(len(ActualArr)) * BytesPerFrame  # Adjust buffer based on recursion depth
    # WorstScenarioMem = len(ActualArr) * BytesPerFrame # Adjust buffer based on recursion depth
    print("Estimated memory usage (bytes)")
    print(" - Best scenario (min): {:.2f} bytes".format(BestScenarioMem))
    # print(" - Worst scenario (max): {:.2f} bytes".format(WorstScenarioMem))
    print("Peak memory usage was {} bytes".format(Peak))
    assert Peak < BestScenarioMem  # Ensure the memory usage is within this range
    return None

@pytest.mark.parametrize(
    "PDataset",
    [
        # (DATASETS[0]),
        (DATASETS[1]),
        (DATASETS[2]),
        # (DATASETS[3]),
        # (DATASETS[4]),
        # (DATASETS[5]),
    ],
)
def test_timing(PDataset: str) -> None:
    OtherAlgorithm = "mergeSort"
    RawArr: list[int] = []
    readValues(PDataset, RawArr)
    print("Comparing {} speed to {}".format(ALGORITHM_NAME, OtherAlgorithm))
    CodeModule = importlib.import_module(EXTRACTED_CODEFILE.rstrip('.py'))
    QuickSortTimeMs = measureTime(getattr(CodeModule, ALGORITHM_NAME), copy.deepcopy(RawArr)) * 1000
    BuiltInSortedTimeMs = measureTime(sorted, copy.deepcopy(RawArr)) * 1000
    print("Timing test with '{}'.".format(PDataset))
    print("Results:")
    print(" - Quick sort(submitted code): {:.3f} ms".format(QuickSortTimeMs))
    print(" - Built-in sorted: {:.3f} ms".format(BuiltInSortedTimeMs))
    assert QuickSortTimeMs > BuiltInSortedTimeMs, "Quick sort shouldn't be faster than the built-in sorted function."
    RawArr.clear()
    return None

"""
Test commands:
# Verbose tests
pytest test_A10_E1.py -v
# Test without silencing print
pytest test_A10_E1.py -s
# Combination
pytest test_A10_E1.py -s -v
"""