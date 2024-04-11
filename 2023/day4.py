def problem1(file):
    lines = []
    with open(file, "r") as f:
        for line in f:
            lines.append(line.strip())

    points = 0

    for line in lines:
        winning, mine = line.split(" | ")

        matches = 0
        winningNums = winning.split()
        for myNum in mine.split():
            if myNum in winningNums:
                matches += 1
        if matches != 0:
            points += 2 ** (matches - 1)

    return int(points)


def problem2(file):
    lines = []
    with open(file, "r") as f:
        for line in f:
            lines.append(line.strip())

    pointMap = {}
    # cardNum - created cards

    def getCardValue(cardNum: int, original: bool) -> int:
        # Already found
        if str(cardNum) in pointMap:
            return pointMap.get(str(cardNum), 0)

        # Need to find
        winning, mine = lines[cardNum - 1].split(" | ")

        matches = 0
        winningNums = winning.split()
        for myNum in mine.split():
            if myNum in winningNums:
                matches += 1

        total = 0
        for i in range(matches):
            total += 1
            total += getCardValue(cardNum + i + 1, False)
        if original:
            pointMap.update({str(cardNum): total})

        return total

    for cardNum in reversed(range(len(lines))):
        getCardValue(cardNum + 1, True)

    return sum(pointMap.values()) + len(lines)


print(problem1("2023/day4.txt"))
print(problem2("2023/day4.txt"))
