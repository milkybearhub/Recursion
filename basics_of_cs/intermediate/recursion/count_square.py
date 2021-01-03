def countSquare(x, y):
    return countSquareHelper(x, y, x * y)

def countSquareHelper(x, y, s):
    if y % x == 0: return s // pow(x, 2)
    return countSquareHelper(y % x, x, s)
