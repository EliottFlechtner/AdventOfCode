def solution_star1():
    res = 0


    return res

def solution_star2(list):
    pass


if __name__ == "__main__":
    with open("2025/input.txt") as f:
        lines = [l.strip().split() for l in f.readlines()]
        print(lines)
        
        results = []
        operators = lines.pop()
        print(operators)
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
        print(sum(results))
