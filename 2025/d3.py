def solution_star1(instructions):
    res = 0
    return res

def solution_star2(instructions):
    res = 0
    return res


if __name__ == "__main__":
    with open("2025/input.txt") as f:
        instrs = []
        ranges = f.read().strip().split(",")

        for r in ranges:
            start, end = map(int, r.split("-"))
            instrs.append((start, end))

        print(f"Instructions: {instrs}")
    # print(f"Solution Star 1: {solution_star1(instrs)}")
    # print(f"Solution Star 2: {solution_star2(instrs)}")