def fizzBuzz(n):
    s = "1"

    for i in range(2, n+1):
        if i % 15 == 0: s += "-FizzBuzz"
        elif i % 3 == 0: s += "-Fizz"
        elif i % 5 == 0: s += "-Buzz"
        else: s += "-" + str(i)

    return s
