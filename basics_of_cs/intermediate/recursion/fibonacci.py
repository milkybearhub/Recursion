def fibonacci(n):
    return fibonacciHelper(0, 1, n)

def fibonacciHelper(fn1, fn2, n):
    if n == 0: return fn1
    return fibonacciHelper(fn2, fn1 + fn2, n - 1)
