def solution_star1(instructions):
    res = 0

    for start, end in instructions:
        for number in range(start, end + 1):
            s_number = str(number)
            length = len(s_number)
            if length % 2 != 0:
                continue
            mid = length // 2
            if s_number[:mid] == s_number[mid:]:
                res += number
    return res

def solution_star2(instructions):
    res = 0
    for start, end in instructions:
        for number in range(start, end + 1):
            s_number = str(number)
            length = len(s_number)
            for k in range(2, length+1):
                cut = length // k
                if s_number[:cut] * k == s_number:
                    res += number
                    break
    return res


if __name__ == "__main__":
    with open("2025/input.txt") as f:
        instrs = []
        ranges = f.read().strip().split(",")

        for r in ranges:
            start, end = map(int, r.split("-"))
            instrs.append((start, end))

        print(f"Instructions: {instrs}")
    print(f"Solution: {solution_star2(instrs)}")