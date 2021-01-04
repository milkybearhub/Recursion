def splitAndAdd(digits):
    if digits <= 0: return digits
    return splitAndAdd(digits // 10) + digits % 10
