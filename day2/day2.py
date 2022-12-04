def whoWon(p1, p2) -> int :
    if p1 == p2:
        return 0
    elif p2 == "Rock" and p1 == "Paper":
        return -1
    elif p2 == "Paper" and p1 == "Scissors":
        return -1
    elif p2 == "Scissors" and p1 == "Rock":
        return -1
    else:
        return 1


shapeScore = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

translations = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

with open('../input/day2/day2.txt') as file:

    points = 0
    for match in file:
        players = match.split()

        p1 = translations[players[0]]
        p2 = translations[players[1]]

        result = whoWon(p1, p2)

        if result > 0:
            points += 6 + shapeScore[p2]
        elif result == 0:
            points += 3 + shapeScore[p2]
        else:
            points += 0 + shapeScore[p2]
    print(points)

        




