alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphaDict = dict.fromkeys(alphabet,0)

with open('../input/day3/day3.txt') as file:
    sumOfAlphabet = 0
    for rucksack in file:
        rucksack = rucksack.replace("\n", "")

        lengthOfSack = len(rucksack)
        halfOfSack = int(lengthOfSack / 2)

        cmp1 = rucksack[0:halfOfSack]
        cmp2 = rucksack[halfOfSack:]

        sharedCharacter = ""
        for character in cmp1:
            if character in cmp2:
                sharedCharacter = character
                break
        sumOfAlphabet += alphabet.index(sharedCharacter)+1
    print(sumOfAlphabet)