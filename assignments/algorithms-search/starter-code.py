"""Starter code for Search Algorithms assignment.

Students: implement `linear_search` and `binary_search` functions.
Run `python starter-code.py` to run a quick demo/benchmark.
"""
from typing import List
import time


def linear_search(arr: List[int], target: int) -> int:
    """Return index of target in arr or -1 if not found. Counts iterations via simple loop."""
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1


def binary_search(arr: List[int], target: int) -> int:
    """Return index of target in sorted arr or -1 if not found."""
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def benchmark_sample():
    import random

    sizes = [10, 100, 1000]
    for n in sizes:
        arr = list(range(n))
        target_present = n - 1
        target_absent = n + 1

        # linear present
        t0 = time.perf_counter()
        linear_search(arr, target_present)
        t1 = time.perf_counter()

        # binary present
        t2 = time.perf_counter()
        binary_search(arr, target_present)
        t3 = time.perf_counter()

        print(f"n={n}: linear_present={(t1-t0):.6f}s, binary_present={(t3-t2):.6f}s")


if __name__ == "__main__":
    print("Quick demo and benchmark")
    benchmark_sample()
