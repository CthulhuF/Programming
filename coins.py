def intCheck(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


while True:

    money = (input("enter purchase cost (from 1 to 99): "))

    if intCheck(money) is False or int(money) > 99 or int(money) < 1:
        print("invalid value entered")
        continue

    else:
        money = int(money)
        change = 100 - money
        numOfCoins = 0
        while True:
            if change >= 50:
                change -= 50
                numOfCoins += 1
            elif change >= 10:
                change -= 10
                numOfCoins += 1
            elif change >= 5:
                change -= 5
                numOfCoins += 1
            elif change >= 1:
                change -= 1
                numOfCoins += 1
            else:
                break

    break

print("number of change coins =", numOfCoins)
# sorry for my English
