from typing import List


def getFull(line: str, pos: int, current: List[str]) -> int:
    if len(line) > pos + 1 and line[pos + 1].isdigit():
        current.append(line[pos + 1])
        return getFull(line, pos + 1, current)
    return int("".join(current))


def problem1(file):
    def check(char):
        return char != "." and not char.isdigit()

    lines = []
    with open(file, "r") as f:
        for line in f:
            lines.append(line.strip())

    total = 0

    for linePos, line in enumerate(lines):
        for charPos, char in enumerate(line):
            # If previous char was digit ignore
            if (
                charPos != 0 and not line[charPos - 1].isdigit() and char.isdigit()
            ) or (charPos == 0 and char.isdigit()):
                num: int = getFull(line, charPos, [char])

                isPart = False

                # Checking Line Above
                if linePos != 0:
                    for index in range(charPos, charPos + len(str(num))):
                        if check(lines[linePos - 1][index]):
                            isPart = True

                # Checking Line Below
                if linePos != len(lines) - 1 and not isPart:
                    for index in range(charPos, charPos + len(str(num))):
                        if check(lines[linePos + 1][index]):
                            isPart = True

                # Checking Line Left + Diagnols
                if (
                    not isPart
                    and charPos != 0
                    and check(line[charPos - 1])
                    or linePos != 0
                    and check(lines[linePos - 1][charPos - 1])
                    or linePos < len(lines) - 1
                    and check(lines[linePos + 1][charPos - 1])
                ):
                    isPart = True

                # Checking Line Right + Diagnols
                if (
                    not isPart
                    and charPos + len(str(num)) < len(line)
                    and (
                        check(line[charPos + len(str(num))])
                        or linePos != 0
                        and check(lines[linePos - 1][charPos + len(str(num))])
                        or linePos < len(lines) - 1
                        and check(lines[linePos + 1][charPos + len(str(num))])
                    )
                ):
                    isPart = True

                if isPart:
                    total += num
    return total


def problem2(file):
    def check(char):
        return char == "*"

    def handleGear(x, y, part):
        if gears.get(f"{x}-{y}"):
            toAdd = gears[f"{x}-{y}"] * part
            gears.pop(f"{x}-{y}")
            return toAdd
        gears.update({f"{x}-{y}": part})
        return 0

    lines = []
    with open(file, "r") as f:
        for line in f:
            lines.append(line.strip())

    ratio = 0
    gears = {}

    for linePos, line in enumerate(lines):
        for charPos, char in enumerate(line):
            # If previous char was digit ignore
            if (
                charPos != 0 and not line[charPos - 1].isdigit() and char.isdigit()
            ) or (charPos == 0 and char.isdigit()):
                num: int = getFull(line, charPos, [char])

                isPart = False

                # Checking Line Above
                if linePos != 0:
                    for index in range(charPos, charPos + len(str(num))):
                        if check(lines[linePos - 1][index]):
                            ratio += handleGear(index, linePos - 1, num)
                            isPart = True
                            break

                # Checking Line Below
                if linePos != len(lines) - 1 and not isPart:
                    for index in range(charPos, charPos + len(str(num))):
                        if check(lines[linePos + 1][index]):
                            ratio += handleGear(index, linePos + 1, num)
                            isPart = True
                            break

                # Checking Line Left + Diagnols
                if not isPart and charPos != 0:
                    if check(line[charPos - 1]):
                        ratio += handleGear(charPos - 1, linePos, num)
                        isPart = True
                    elif linePos != 0 and check(lines[linePos - 1][charPos - 1]):
                        ratio += handleGear(charPos - 1, linePos - 1, num)
                        isPart = True
                    elif linePos < len(lines) - 1 and check(
                        lines[linePos + 1][charPos - 1]
                    ):
                        ratio += handleGear(charPos - 1, linePos + 1, num)

                # Checking Line Right + Diagnols
                if not isPart and charPos + len(str(num)) < len(line):
                    if check(line[charPos + len(str(num))]):
                        ratio += handleGear(charPos + len(str(num)), linePos, num)
                        isPart = True
                    elif linePos != 0 and check(
                        lines[linePos - 1][charPos + len(str(num))]
                    ):
                        ratio += handleGear(charPos + len(str(num)), linePos - 1, num)
                        isPart = True
                    elif linePos < len(lines) - 1 and check(
                        lines[linePos + 1][charPos + len(str(num))]
                    ):
                        ratio += handleGear(charPos + len(str(num)), linePos + 1, num)
                        isPart = True

    return ratio

print(problem1("2023/day3.txt"))
print(problem2("2023/day3.txt"))
