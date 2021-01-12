def notDivided(x,y):
    # 1人のクラスは考慮しない
    numbers = "1"

    for i in range(2, x + 1):
        if i % y != 0: numbers += "-" + str(i)

    return numbers
