# Fibonacci

import time


def fib_dp(n, memo):
    # 0.00027 sec for n=40
    # 27.72 sec for n=40000
    if n<3:
        return 1
    if memo[n] != 0:
        return memo[n]
    memo[n-2] = fib_dp(n-2, memo)
    memo[n-1] = fib_dp(n-1, memo)
    return memo[n-2] + memo[n-1]

def fib_recur(n):
    # 29.56 sec for n=40
    if n<3:
        return 1
    return fib_recur(n-2)+fib_recur(n-1)


def main():
    max_int = 40000
    memo = [0] * max_int

    t0 = time.perf_counter()
    for i in range(0,max_int):
        print(f"fib {i}: {fib_dp(i, memo)}")
    t1 = time.perf_counter() - t0
    print(f"Elapsed time: {t1}")

main()
