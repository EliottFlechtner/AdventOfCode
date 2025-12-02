def max_index(l):
    m = -1
    idx = -1
    for i in range(len(l)):
        e = l[i]
        if e > m:
            m = e
            idx = i
    return idx, m

def solution_star1(banks):
    res = 0
    for bank in banks:
        max1_pos, max1 = max_index(bank)
        rsub = bank[max1_pos+1:]
        if rsub == []:
            res += max(bank[:max1_pos]) * 10 + max1
        else:
            res += max1 * 10 + max(rsub)
    return res

def compute_sum(maxes):
    str_ = str(maxes)
    return str_[1:len(str_)-1].replace(", ", "")

def solution_star2(banks):
    res = 0
    for bank in banks:
        maxes = []
        k = 2
        start = 0
        while k > 0:
            max_pos, max_val = max_index(bank[start:len(bank)-k+1])
            maxes.append(max_val)
            start += max_pos + 1
            k -= 1
        res += int(compute_sum(maxes))
    return res

if __name__ == "__main__":
    with open("2025/input.txt") as f:
        banks = [[int(line[i]) for i in range(len(line.strip()))] for line in f.readlines()]

    # print(f"Solution Star 1: {solution_star1(banks)}")
    print(f"Solution Star 2: {solution_star2(banks)}")