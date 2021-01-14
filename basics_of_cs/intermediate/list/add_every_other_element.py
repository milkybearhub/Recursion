def addEveryOtherElement(intArr):
    sum = 0
    for i in intArr[0::2]: sum += i
    return sum
