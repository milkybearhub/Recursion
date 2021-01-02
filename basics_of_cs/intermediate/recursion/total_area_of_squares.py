def totalSquareArea(x):
    if x <= 0: return 0
    return pow(x, 3) + totalSquareArea(x - 1)
