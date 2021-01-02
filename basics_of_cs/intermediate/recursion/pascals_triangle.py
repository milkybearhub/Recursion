def numberOfDots(x):
    if x <= 0: return 0
    return numberOfDots(x - 1) + x
