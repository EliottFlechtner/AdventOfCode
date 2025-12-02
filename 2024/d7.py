def find_calibration_result(operations):
    reachable_target = []
    for op in operations:
        target, numbers = op[0], op[1]
        attempts = 2 ** (len(numbers) - 1)
        for i in range(attempts):
            binstr = str(bin(i))[2:].zfill(len(numbers) - 1)
            x = numbers[0]
            k = 1
            for c in binstr:
                if c == "0":
                    x += numbers[k]
                else:
                    x *= numbers[k]
                k += 1
            if x == target:
                reachable_target.append(target)
                break
    return sum(reachable_target)


def to_base3_string(n):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % 3))
        n //= 3
    return "".join(reversed(digits))


def concatenate_numbers(a, b):
    return a * (10 ** (len(str(b)))) + b


def find_calibration_result2(operations):
    reachable_target = []
    for op in operations:
        target, numbers = op[0], op[1]
        max_k = len(numbers) - 1
        attempts = 3**max_k
        for i in range(attempts):
            b3str = to_base3_string(i).zfill(max_k)
            x = numbers[0]
            k = 1
            for c in b3str:
                if c == "0":
                    x += numbers[k]
                elif c == "1":
                    x *= numbers[k]
                elif c == "2":
                    x = concatenate_numbers(x, numbers[k])
                k += 1
            if x == target:
                reachable_target.append(target)
                break
    return sum(reachable_target)


if __name__ == "__main__":
    with open("2024/input.txt") as f:
        operations = [
            (int(left), list(map(int, right.split())))
            for line in f.readlines()
            for left, right in [line.strip().split(": ")]
        ]
        # print(find_calibration_result(operations))
        print(find_calibration_result2(operations))
