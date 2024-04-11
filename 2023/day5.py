def problem1(file):
    lines = []
    with open(file, "r") as f:
        for line in f:
            lines.append(line.strip())

    seeds = [int(x) for x in lines[0].split(": ")[1].split()]

    filters = []

    start = False
    filter = 0
    for line in lines[2:]:
        if line.strip() == "":
            start = False
        # dest, src, range
        if start:
            filters[filter - 1].append([int(x) for x in line.split()])

        if line.endswith("map:"):
            filter += 1
            filters.append([])
            start = True

    location = 9223372036854775807

    for seed in seeds:
        current = seed
        for filterSet in filters:
            for filter in filterSet:
                if filter[1] <= current <= filter[1] + filter[2]:
                    # 50 98 2
                    current = filter[0] + (current - filter[1])
                    break
        location = min(location, current)

    return location


def problem2(file):
    lines = []
    with open(file, "r") as f:
        for line in f:
            lines.append(line.strip())

    seeds = []

    data = lines[0].split(": ")[1].split()
    for i in range(len(data)):
        start, added = (data[i * 2], data[i * 2 + 1])
        for j in range(int(added)):
            seeds.append(int(start) + j)

    print(len(seeds))

    filters = []

    start = False
    filter = 0
    for line in lines[2:]:
        if line.strip() == "":
            start = False
        # dest, src, range
        if start:
            filters[filter - 1].append([int(x) for x in line.split()])

        if line.endswith("map:"):
            filter += 1
            filters.append([])
            start = True

    location = 9223372036854775807

    for seed in seeds:
        current = seed
        for filterSet in filters:
            for filter in filterSet:
                if filter[1] <= current <= filter[1] + filter[2]:
                    # 50 98 2
                    current = filter[0] + (current - filter[1])
                    break
        location = min(location, current)

    return location


print(problem2("2023/day5.txt"))
