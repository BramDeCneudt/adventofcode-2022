

with open('../input/day1/day1.txt') as file:

    totalAmountList = []
    total = 0

    for calorie in file:
        if calorie == "\n":
            totalAmountList.append(total)
            total = 0
        else:
            total += int(calorie)
    # it doesn't add the last on to the list
    totalAmountList.append(total)    

    totalTopThree = 0
    for maxIndex in range(3):
        maxAmount = max(totalAmountList)
        totalTopThree += maxAmount
        totalAmountList.remove(maxAmount)
    print(totalTopThree)
