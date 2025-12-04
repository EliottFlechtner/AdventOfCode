def count_neighbors(grid, dims, i, j):
    dirs = {(-1, -1), (-1, 0), (-1, 1), (+0, -1), (+0, 1), (+1, -1), (+1, 0), (+1, 1)}
    h, w = dims
    c = 0
    for dir in dirs:
        dx, dy = dir
        ni, nj = i + dx, j + dy

        if ni >= h or ni < 0:
            continue
        if nj >= w or nj < 0:
            continue

        c += grid[ni][nj] == "@"
    return c


def solution_star1(grid):
    res = 0
    h, w = len(grid), len(grid[0])
    new_grid = [["." for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "@":
                neighbors = count_neighbors(grid, (h, w), i, j)
                if neighbors < 4:
                    new_grid[i][j] = "x"
                    res += 1
                else:
                    new_grid[i][j] = "@"
    return new_grid, res


def solution_star2(grid):
    res = 0
    while True:
        new_grid, count = solution_star1(grid)
        grid = new_grid
        res += count
        if count == 0:
            break
    return grid, res


def pretty_print(grid):
    for row in grid:
        print("".join(row))

if __name__ == "__main__":
    with open("2025/input.txt") as f:
        grid = [line.strip() for line in f.readlines()]

    pretty_print(grid)

    new_grid, star1_res = solution_star1(grid)
    print(f"Solution Star 1: {star1_res}")

    pretty_print(new_grid)

    final_grid, star2_res = solution_star2(new_grid)

    print(f"Solution Star 2: {star2_res+star1_res}")

    pretty_print(final_grid)