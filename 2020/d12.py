NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

DIRECTIONS = ['N', 'E', 'S', 'W']  # Direction mapping
FACING = EAST
X, Y = 0, 0

OPERATORS = ["F", "R", "L"]

def move_towards(dir, dist):
    global X, Y
    if dir == 'N':
        Y += dist
    elif dir == 'S':
        Y -= dist
    elif dir == 'W':
        X -= dist
    elif dir == 'E':
        X += dist

def rotate_towards(dir, angle):
    global FACING
    steps = angle // 90
    if dir == 'L':
        steps = -steps  # Left rotation is negative
    FACING = (FACING + steps) % 4

def read_instructions(instructions):
    global X, Y, FACING
    for dir, val in instructions:
        if dir in DIRECTIONS:
            move_towards(dir, val)
        elif dir == 'F':
            move_towards(DIRECTIONS[FACING], val)
        elif dir in OPERATORS:
            rotate_towards(dir, val)
        # print(X, Y, DIRECTIONS[FACING])
    return compute_manhattan((0, 0), (X, Y))

def compute_manhattan(init, final):
    (xi, yi), (xf, yf) = init, final
    return abs(xi - xf) + abs(yi - yf)

if __name__ == "__main__":
    with open("2020/input.txt") as f:
        instructions = [(s[0], int(s[1:])) for s in f.readlines()]
        print(instructions)
        print(read_instructions(instructions))
