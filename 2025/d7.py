def solution_star1(grid):
    res = 0
    start = grid[0].index("S")
    grid[1][start] = "|"

    for row in range(1, len(grid) - 1):
        for i, c in enumerate(grid[row]):
            if c == ".":
                continue
            elif c == "|":
                if grid[row + 1][i] == "^":
                    if i-1 >= 0 and grid[row + 1][i-1] == ".":
                        grid[row + 1][i-1] = "|"
                        split = True
                    if i+1 < len(grid[row + 1]) and grid[row + 1][i+1] == ".":
                        grid[row + 1][i+1] = "|"
                        split = True
                    if split:
                        res += 1
                        split = False
                elif grid[row + 1][i] == ".":
                    grid[row + 1][i] = "|"
    return res

def solution_star2(grid):
    # Count paths using memoization to avoid exponential recursion
    memo = {}
    
    def count_paths(row, col):
        if (row, col) in memo:
            return memo[(row, col)]
        
        if row == len(grid) - 1:
            return 1
        
        cell = grid[row][col]
        
        if cell == ".":
            result = count_paths(row + 1, col)
        elif cell == "^":
            paths = 0
            # Check left
            if col - 1 >= 0 and grid[row + 1][col - 1] == ".":
                paths += count_paths(row + 1, col - 1)
            # Check right
            if col + 1 < len(grid[row]) and grid[row + 1][col + 1] == ".":
                paths += count_paths(row + 1, col + 1)
            result = paths
        else:
            result = 0
        
        memo[(row, col)] = result
        return result
    
    start = grid[0].index("S")
    return count_paths(1, start)


def pretty_print(grid):
    for row in grid:
        print("".join(row))

if __name__ == "__main__":
    with open("2025/input.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    # result_star1 = solution_star1(grid)
    # print("Star 1:", result_star1)

    result_star2 = solution_star2(grid)
    print("Star 2:", result_star2)