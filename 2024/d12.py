import helpers as h

visited = set()


def crop(crops, target, x, y):
    if x < 0 or y < 0 or x >= len(crops) or y >= len(crops[0]):
        return 0, 1  # Out of bounds, contributes to perimeter
    if crops[x][y] != target:
        return 0, 1  # Different crop, contributes to perimeter
    if (x, y) in visited:
        return 0, 0  # Already visited, no additional area or perimeter

    visited.add((x, y))
    area, perimeter = 1, 0
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        a, p = crop(crops, target, x + dx, y + dy)
        area += a
        perimeter += p
    return area, perimeter


def find_crops_area_perimeter(crops):
    l1, l2 = len(crops), len(crops[0])
    s = 0
    for i in range(l1):
        for j in range(l2):
            if (i, j) not in visited:
                area, perimeter = crop(crops, crops[i][j], i, j)
                s += area * perimeter
    return s


def crop2(crops, target, x, y):
    if x < 0 or y < 0 or x >= len(crops) or y >= len(crops[0]):
        return 0, 1  # Out of bounds, contributes to perimeter
    if crops[x][y] != target:
        return 0, 1  # Different crop, contributes to perimeter
    if (x, y) in visited:
        return 0, 0  # Already visited, no additional area or perimeter

    visited.add((x, y))
    area, sides = 1, 0
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        a, s = crop(crops, target, x + dx, y + dy)
        area += a
        sides += s
    return area, sides


def find_crops_area_sides(crops):
    l1, l2 = len(crops), len(crops[0])
    s = 0
    for i in range(l1):
        for j in range(l2):
            if (i, j) not in visited:
                area, sides = crop(crops, crops[i][j], i, j)
                s += area * sides
    return s


from collections import deque

def get_regions_and_areas(grid):
    """
    Finds all regions in the grid and computes their areas.
    Returns a list of regions where each region is a list of coordinates.
    """
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def bfs(start):
        queue = deque([start])
        visited[start[0]][start[1]] = True
        region = [start]
        plant_type = grid[start[0]][start[1]]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == plant_type:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    region.append((nr, nc))
        return region
    
    regions = []
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                region = bfs((r, c))
                regions.append(region)
    return regions

def calculate_sides(grid, region):
    """
    Calculates the number of sides for a given region.
    """
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    sides = 0
    
    for r, c in region:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != grid[r][c]:
                sides += 1
    return sides

def calculate_total_price(grid):
    """
    Calculates the total price of fencing all regions on the map.
    """
    regions = get_regions_and_areas(grid)
    total_price = 0
    
    for region in regions:
        area = len(region)
        sides = calculate_sides(grid, region)
        price = area * sides
        total_price += price
    
    return total_price


if __name__ == "__main__":
    crops = h.read_input_list_str("2024/input.txt")
    print(crops)
    print(calculate_total_price(crops))
