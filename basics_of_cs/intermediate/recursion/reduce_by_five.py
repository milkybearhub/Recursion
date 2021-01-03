def reduceByFive(n):
    return reduceByFiveHelper(n, n)

def reduceByFiveHelper(n, origin):
    if n < 0: return increaseByFive(n, origin)
    print(n)
    return reduceByFiveHelper(n - 5, origin)

def increaseByFive(n, origin):
    if n == origin: return origin
    print(n)
    return increaseByFive(n + 5, origin)

16,11,6,1,-4,1,6,11,16
print(reduceByFive(16))
# 9 → 9,4,-1,4,9
print(reduceByFive(9))
# 5 → 5,0,-5,0,5
print(reduceByFive(5))
