"""
Fibonacci Number Computation - Four Approaches Compared
Runs for n = 10, 100, 1000, 10000, 100000
"""

import time
import sys

sys.setrecursionlimit(200000)


# ---------- Method 1: Naive recursion ----------
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# ---------- Method 2: Memoized recursion ----------
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# ---------- Method 3: Iterative DP ----------
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# ---------- Method 4: Fast doubling ----------
def fib_fast_doubling(n):
    def helper(k):
        if k == 0:
            return (0, 1)
        a, b = helper(k // 2)
        c = a * (2 * b - a)
        d = a * a + b * b
        if k % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)
    return helper(n)[0]


def show(label, value, t):
    digits = len(str(value))
    if digits > 50:
        print(f"  {label:<20}: {digits} digits (too large to print) | {t:.6f} sec")
    else:
        print(f"  {label:<20}: {value} | {t:.6f} sec")


def main():
    values_of_n = [10, 100, 1000, 10000, 100000]

    for n in values_of_n:
        print(f"\n{'='*60}")
        print(f"Fibonacci(n={n})")
        print(f"{'='*60}")

        # Fast doubling (always feasible, use as reference)
        start = time.time()
        result_fast = fib_fast_doubling(n)
        t_fast = time.time() - start

        # Iterative DP (always feasible)
        start = time.time()
        result_iter = fib_iterative(n)
        t_iter = time.time() - start

        show("Fast doubling", result_fast, t_fast)
        show("Iterative DP", result_iter, t_iter)

        # Sanity check: both methods must agree
        assert result_fast == result_iter, "Mismatch between fast doubling and iterative DP!"

        # Memoized recursion — skip only for n=100000 (stack overflow risk)
        if n <= 10000:
            start = time.time()
            result_memo = fib_memo(n)
            t_memo = time.time() - start
            show("Memoized recursion", result_memo, t_memo)
            assert result_memo == result_iter, "Mismatch in memoized recursion!"
        else:
            print(f"  {'Memoized recursion':<20}: skipped (recursion depth too high)")

        # Naive recursion — skip beyond n=30 (exponential blow-up)
        if n <= 30:
            start = time.time()
            result_naive = fib_naive(n)
            t_naive = time.time() - start
            show("Naive recursion", result_naive, t_naive)
            assert result_naive == result_iter, "Mismatch in naive recursion!"
        else:
            print(f"  {'Naive recursion':<20}: skipped (would take too long, O(2^n))")

    print(f"\n{'='*60}")
    print("Done. All computed results matched across methods.")


if __name__ == "__main__":
    main()
