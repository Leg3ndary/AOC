def part_one():
    total = 0
    for line in open("2023/day1.txt"):
        stuff = []
        for char in line:
            if char.isdigit():
                stuff.append(char)
                break

        for char in line[::-1]:
            if char.isdigit():
                stuff.append(char)
                break

        total += int("".join(stuff))

    print(total)


def part_two():
    total = 0
    for line in open("2023/day1.txt"):
        num = 0

        fixed_line = (
            line.replace("one", "o1e")
            .replace("two", "t2o")
            .replace("three", "t3e")
            .replace("four", "f4r")
            .replace("five", "f5e")
            .replace("six", "s6x")
            .replace("seven", "s7n")
            .replace("eight", "e8t")
            .replace("nine", "n9e")
        )

        for char in fixed_line:
            if char.isdigit():
                num += int(char) * 10
                break

        for char in fixed_line[::-1]:
            if char.isdigit():
                num += int(char)
                break
        total += num

    print(total)


part_one()
part_two()
