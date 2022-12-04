def fixMatch(p1, fix) -> str :
    if fix == 1: 
        return shapeWeakness[p1]
    elif fix == 0:
        return p1
    elif fix == -1:
        return shapeStrength[p1]
    else:
        raise Exception("unexpected output: " + fix + " " + p1)


shapeStrength = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}

shapeWeakness = {
    "Rock": "Paper",
    "Paper": "Scissors",
    "Scissors": "Rock"
}



shapeScore = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

translations = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": -1,
    "Y": 0,
    "Z": 1,
}

with open('../input/day2/day2.txt') as file:

    points = 0
    for match in file:
        players = match.split()

        p1 = translations[players[0]]
        fix = translations[players[1]]

        p2 = fixMatch(p1, fix)

        if fix > 0:
            points += 6 + shapeScore[p2]
        elif fix == 0:
            points += 3 + shapeScore[p2]
        else:
            points += 0 + shapeScore[p2]
    print(points)

        




