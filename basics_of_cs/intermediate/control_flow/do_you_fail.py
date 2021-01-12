def doYouFail(string):
    count = 0
    judge = "pass"

    for char in string:
        if count >= 3:
            judge = "fail"
            break

        if char == "A": count += 1

    return judge

# A:Absence
# P:Participate
