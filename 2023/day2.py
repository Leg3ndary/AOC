def problem1(file):
    lines = []
    with open(file, "r") as f:
        for line in f:
            lines.append(line.strip())

    gameids = 0

    for gameID, data in enumerate(lines):
        data = data.split(": ")[1]
        sets = data.split("; ")

        possible = True

        for set_game in sets:
            colours = set_game.split(", ")
            for piece in colours:
                num, colour = piece.split()
                num = int(num)

                if (
                    colour == "red"
                    and num > 12
                    or colour == "green"
                    and num > 13
                    or colour == "blue"
                    and num > 14
                ):
                    possible = False
                    break

            if not possible:
                break

        if possible:
            gameids += gameID + 1

    # 12 red 13 green 14 blue

    return gameids


def problem2(file):
    lines = []
    with open(file, "r") as f:
        for line in f:
            lines.append(line.strip())

    sum = 0

    for data in lines:
        data = data.split(": ")[1]
        sets = data.replace(";", ",")

        red = 0
        green = 0
        blue = 0

        for pieces in sets.split(", "):
            num, colour = pieces.split()
            num = int(num)

            if colour == "red":
                red = max(num, red)
            elif colour == "green":
                green = max(num, green)
            elif colour == "blue":
                blue = max(num, blue)

        sum += red * green * blue

    return sum


print(problem1("2023/day2.txt"))
print(problem2("2023/day2.txt"))
