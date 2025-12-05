def solution_star1(ranges, values):
    res = 0

    for v in values:
        for r in ranges:
            if r[0] <= v <= r[1]:
                res += 1
                break
    return res


def solution_star2(ranges):
    merged = []
    sorted_ranges = sorted(ranges, key=lambda x: x[0])

    for r in sorted_ranges:
        if not merged or merged[-1][1] < r[0]:
            merged.append(r)
        else:
            merged[-1][1] = max(merged[-1][1], r[1])
        print(merged)

    total_covered = sum(r[1] - r[0] + 1 for r in merged)
    return total_covered


if __name__ == "__main__":
    with open("2025/input.txt") as f:
        vals = f.read().split("\n\n")

    ranges = [list(map(int, line.split("-"))) for line in vals[0].splitlines()]
    values = [int(line) for line in vals[1].splitlines()]

    print(ranges, values)

    # star1_res = solution_star1(ranges, values)
    # print(f"Solution Star 1: {star1_res}")

    star2_res = solution_star2(ranges)
    print(f"Solution Star 2: {star2_res}")
