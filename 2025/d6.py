def solution_star1(lines):
    results = []

    operators = lines.pop()
    for i, line in enumerate(lines):
        numbers = list(map(int, line))
        if i == 0:
            results.extend(numbers)
        else:
            for k in range(len(numbers)):
                op = operators[k]
                print(f"Applying {op} to {results[k]} and {numbers[k]}")
                if op == '+':
                    results[k] += numbers[k]
                elif op == '*':
                    results[k] *= numbers[k]
    return sum(results)

def reprocess_input(nums):
    for i in range(len(nums)):
        nums[i] = list(map(int, nums[i]))

    results = []
    for i, line in enumerate(nums):
        for j in range(len(line)):
            print(f"Processing line {i}, number {j}: {line[j]}")
    return nums

def solution_star2(lines):
    results = []
    operators = lines.pop()
    print(reprocess_input(lines))

    # for i, line in enumerate(lines):
    #     numbers = list(map(int, line))
    #     if i == 0:
    #         results.extend(numbers)
    #     else:
    #         for k in range(len(numbers)):
    #             op = operators[k]
    #             print(f"Applying {op} to {results[k]} and {numbers[k]}")
    #             if op == '+':
    #                 results[k] += numbers[k]
    #             elif op == '*':
    #                 results[k] *= numbers[k]
    return sum(results)


if __name__ == "__main__":
    lines = []
    with open("2025/input.txt") as f:
        lines = [l.strip().split() for l in f.readlines()]
        
    print("Star 2:", solution_star2(lines))
