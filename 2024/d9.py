import helpers as h

def expand_section(disk_map, expanded, fid, i):
    x = int(disk_map[i])
    for _ in range(x):
        expanded.append(fid if i % 2 == 0 else None)
    return fid + 1 if i % 2 == 0 else fid

def print_memory_map(disk_map):
    for e in disk_map:
        print("." if e is None else e, end="")
    print()

def identify_ranges(disk_map):
    free = []
    blocks = []
    i = 0

    while i < len(disk_map):
        beg = i
        if disk_map[i] is None:
            while i < len(disk_map) and disk_map[i] is None:
                i += 1
            free.append((beg, i - beg))
        else:
            current_value = disk_map[i]
            while i < len(disk_map) and disk_map[i] == current_value:
                i += 1
            blocks.append((beg, i - beg))
    return free, blocks[::-1]

def rearrange_disk_map(disk_map):
    expanded = []
    fid = 0
    for i in range(len(disk_map)):
        fid = expand_section(disk_map, expanded, fid, i)
    free, blocks = identify_ranges(expanded)
    filesystem = expanded.copy()
    for i in range(len(blocks)):
        beg, size = blocks[i]
        for j in range(len(free)):
            fbeg, fsize = free[j]
            if fsize >= size:
                for k in range(size):
                    filesystem[fbeg + k] = filesystem[beg+k]
                    filesystem[beg + k] = None
                free[j] = (fbeg + size, fsize - size)
                break
    print_memory_map(filesystem)
    return filesystem

def find_filesystem_checksum(disk_map):
    filesystem = rearrange_disk_map(disk_map)
    return sum(i*filesystem[i] for i in range(len(filesystem)) if filesystem[i] is not None)

if __name__ == "__main__":
    disk_map = h.read_input_list_int("2024/input.txt")[0]
    print(disk_map)
    print(find_filesystem_checksum(disk_map))
