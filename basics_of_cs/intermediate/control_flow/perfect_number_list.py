def perfectNumberList(n):
    half = n / 2
    output = ""

    for i in range(1, n+1):
        sum = 0
        divisor = 1
        while divisor <= i / 2:
            if i != divisor and i % divisor == 0: sum += divisor
            divisor += 1
        if i == sum: output += str(sum) + "-"

    return output[:-1]
