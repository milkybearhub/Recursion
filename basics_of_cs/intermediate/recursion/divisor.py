def divisor(number):
    return divisorHelper(number, number)

def divisorHelper(number, count):
    if count == 1: return count
    if number % count != 0: return str(divisorHelper(number, count - 1)) 
    return str(divisorHelper(number, count - 1)) + '-' + str(count)
