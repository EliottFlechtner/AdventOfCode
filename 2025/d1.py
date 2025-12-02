def find_password(instructions):
    pos = 50
    pwd = 0
    
    for dir, n in instructions:
        step = 1 if dir == 'R' else -1
        for _ in range(n):
            pos = (pos + step) % 100
            if pos == 0:
                pwd += 1
    return pwd

if __name__ == "__main__":
    with open("2025/input.txt") as f:
        instrs = []
        for line in f.readlines():
            instrs.extend((e[0], int(e[1:])) for e in line.split())
    print(f"Password: {find_password(instrs)}")