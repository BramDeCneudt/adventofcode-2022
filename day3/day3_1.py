alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphaDict = dict.fromkeys(alphabet,0)

with open('../input/day3/day3.txt') as file:
    
    rucksacks = []
    for rucksack in file:
        rucksack = rucksack.replace("\n", "")

        rucksacks.append(rucksack)
    
    sum = 0
    totalLoops = int(len(rucksacks) / 3)
    for index in range(totalLoops):

        begin = index*3
        # print(begin, begin+1, begin+2)
        sharedCharacter = ""
        for character in rucksacks[begin]:
            if character in rucksacks[begin+1] and character in rucksacks[begin+2]:
                sharedCharacter = character
                sum += alphabet.index(sharedCharacter)+1
                break
    print(sum)