import helpers as h

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find_trailheads(topographic_map):
    return [
        (i, j)
        for i in range(len(topographic_map))
        for j in range(len(topographic_map[0]))
        if topographic_map[i][j] == 0
    ]


def find_trailheads_scores(topographic_map):
    trailheads = find_trailheads(topographic_map)

    def is_valid_move(x, y):
        return (
            0 <= x < len(topographic_map)
            and 0 <= y < len(topographic_map[0])
            and topographic_map[x][y] != '.'
        )

    def trail(visited, target, x, y):
        if not is_valid_move(x, y): #or (x, y) in visited:
            return 0
        
        visited.add((x, y))
        if topographic_map[x][y] == 9:
            return 1
        
        reachable_nines = 0
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny) and topographic_map[nx][ny] == topographic_map[x][y] + 1:
                reachable_nines += trail(visited, target + 1, nx, ny)
        return reachable_nines
    
    scores = []
    for sx, sy in trailheads:
        visited = set()
        score = trail(visited, 1, sx, sy)
        scores.append(score)
    print(scores)
    return sum(scores)


if __name__ == "__main__":
    with open("2024/input.txt") as f:
        topographic_map = [[int(i) if i != '.' else i for i in x ] for x in f.read().splitlines()]
    
    print(topographic_map)
    print(find_trailheads_scores(topographic_map))
