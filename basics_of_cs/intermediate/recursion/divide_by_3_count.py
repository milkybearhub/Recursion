def divideBy3Count(n):
    if n == 1: return 0
    return divideBy3Count(n // 3) + 1
