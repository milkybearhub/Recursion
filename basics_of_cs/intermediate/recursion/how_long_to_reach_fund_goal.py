def howLongToReachFundGoal(capitalMoney,goalMoney,interest):
    return howLongToReachFundGoalHelper(capitalMoney, goalMoney, interest, 0)

def howLongToReachFundGoalHelper(capitalMoney, goalMoney, interest, year):
    if goalMoney <= capitalMoney: return year
    if year >= 80: return 80

    if year % 2 == 0: goalMoney *= 1.02
    else: goalMoney *= 1.03

    return howLongToReachFundGoalHelper(capitalMoney * (1 + interest/100), goalMoney, interest, year + 1)
