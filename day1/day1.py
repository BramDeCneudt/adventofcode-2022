

with open('../input/day1/day1.txt') as file:

    totalAmountList = []
    total = 0

    for calorie in file:
        if calorie == "\n":
            totalAmountList.append(total)
            total = 0
        else:
            total += int(calorie)
    print(max(totalAmountList))
