import helpers as h


def find_antennas_positions(antennas_map):
    antennas_positions = []
    for i in range(len(antennas_map)):
        for j in range(len(antennas_map[i])):
            c = antennas_map[i][j]
            if c != ".":
                antennas_positions.append((c, i, j))
    return antennas_positions


def check_in_map(antennas_map, x, y):
    return x >= 0 and y >= 0 and x < len(antennas_map) and y < len(antennas_map[0])


def check_if_free(antennas_map, x, y):
    return check_in_map(antennas_map, x, y) and antennas_map[x][y] in "."


def place(antennas_map, x, y, antinode="#"):
    if check_in_map(antennas_map, x, y):
        if check_if_free(antennas_map, x, y):
            antennas_map[x][y] = antinode
        elif antennas_map[x][y] == antinode:
            return False
        return True
    return False


def place_antinode_on_map(antennas_map, c1, c2, antinode="#"):
    freq1, x1, y1 = c1
    freq2, x2, y2 = c2
    diff_x = x2 - x1
    diff_y = y2 - y1

    if freq1 != freq2:
        return 0

    return place(antennas_map, x1 - diff_x, y1 - diff_y, antinode) + place(
        antennas_map, x2 + diff_x, y2 + diff_y, antinode
    )


def place_antinode_on_map_harmonics(antennas_map, placed, c1, c2, antinode="#"):
    freq1, x1, y1 = c1
    freq2, x2, y2 = c2
    diff_x = x2 - x1
    diff_y = y2 - y1

    if freq1 != freq2:
        return

    placed.add((x1, y1))
    placed.add((x2, y2))

    current_x, current_y = x1, y1
    while check_in_map(antennas_map, current_x - diff_x, current_y - diff_y):
        current_x -= diff_x
        current_y -= diff_y
        if place(antennas_map, current_x, current_y, antinode):
            placed.add((current_x, current_y))

    current_x, current_y = x2, y2
    while check_in_map(antennas_map, current_x + diff_x, current_y + diff_y):
        current_x += diff_x
        current_y += diff_y
        if place(antennas_map, current_x, current_y, antinode):
            placed.add((current_x, current_y))


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


def solvep1(antennas_map):
    placed = 0
    antennas_positions = find_antennas_positions(antennas_map)

    for i in range(len(antennas_positions)):
        for j in range(i + 1, len(antennas_positions)):
            print(antennas_positions[i], antennas_positions[j])
            placed += place_antinode_on_map(
                antennas_map, antennas_positions[i], antennas_positions[j]
            )
    print_matrix(antennas_map)
    return placed


def solvep2(antennas_map):
    placed = set()
    antennas_positions = find_antennas_positions(antennas_map)

    for i in range(len(antennas_positions)):
        for j in range(i + 1, len(antennas_positions)):
            place_antinode_on_map_harmonics(
                antennas_map, placed, antennas_positions[i], antennas_positions[j]
            )
    print_matrix(antennas_map)
    return len(placed)


if __name__ == "__main__":
    antennas_map = h.read_input_list_str("2024/input.txt")
    print(solvep2(antennas_map))
