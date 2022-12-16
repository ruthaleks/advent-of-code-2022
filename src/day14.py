INPUT_FILE_PATH = "input/d14.txt"

import sys

def main():
    input = parse_input()
    print("Part 1 = ", simulation(input))
    print("Part 2 = ", simulation_with_inf_floor(input))

def simulation(input:list):
    grid, y_max = create_grid(input)
    units = 0
    cont = True
    while cont:
        cont = add_one_unit_sand(grid, y_max)
        units += 1
    #print_grid(input, grid)
    return units-1

def simulation_with_inf_floor(input:list):
    grid, y_max = create_grid(input)
    units = 0
    while grid.get((500, 0)) == None:
        add_one_unit_sand_with_inf_floor(grid, y_max)
        units += 1
    #print_grid(input, grid)
    return units

def add_one_unit_sand(grid: dict, y_max:int):
    source = (500, 0)
    current = source
    cont = True
    while cont:
        current, cont, inside_grid = next_pos(current, grid, y_max)
    if current != None:
        assert grid.get(current) == None
        grid[current] = 'o'
    return inside_grid

def add_one_unit_sand_with_inf_floor(grid: dict, y_max:int, with_floor:bool=False):
    source = (500, 0)
    current = source
    cont = True
    while cont:
        current, cont, inside_grid = next_pos(current, grid, y_max)
    if current != None:
        assert grid.get(current) == None
        grid[current] = 'o'
    return current != None

def next_pos(current:tuple, grid:dict, y_max:int):
    (x, y) = current
    next = (x, y+1)
    if next[1] >= y_max:
        return current, False, False
    if is_air(next, grid):
        return next, True, True
    if is_air(get_left(next), grid):
        return get_left(next), True, True
    if is_air(get_right(next), grid):
        return get_right(next), True, True
    return current, False, True

def is_air(pos:tuple, grid:dict):
    return grid.get(pos) == None

def get_left(pos:tuple):
    return (pos[0]-1, pos[1])

def get_right(pos:tuple):
    return (pos[0]+1, pos[1])

def grid_size(input:list):
    x_max = 0
    y_max = 0
    x_min = sys.maxsize
    for row in input:
        (x, y) = max(row,key=lambda item:item[0])
        x_max = max(x, x_max)
        (x, y) = min(row,key=lambda item:item[0])
        x_min = min(x, x_min)
        (x, y) = max(row,key=lambda item:item[1])
        y_max = max(y, y_max)

    return x_max, x_min, y_max

def create_grid(input:list):
    x_max, x_min, y_max = grid_size(input)
    lines = [item for sublist in list(map(get_lines, input)) for item in sublist]
    grid = {}
    for y in range(0, y_max+1):
        for x in range(x_min, x_max+1):
            if (x,y) in lines:
                grid[(x,y)] = '#'
    return grid, y_max+2

def add_floor(input:list, grid:dict):
    x_max, x_min, y_max = grid_size(input)
    for x in range(x_min, x_max+1):
        grid[(x,y_max)] = '#'
    return grid

def print_grid(input:list, grind:dict):
    x_max, x_min, y_max = grid_size(input)
    x_max += 10
    y_max += 3
    x_min -= 10
    for y in range(0, y_max+1):
        row = ""
        for x in range(x_min, x_max+1):
            val = grind.get((x,y))
            if val == None:
                val = '.'
            row = row + val
        print(row)


def get_lines(points: list):
    coord = []
    for i in range(0, len(points)-1):
        if points[i][0] == points[i+1][0]:
            coord = coord + get_vertical_line(points[i], points[i+1])
        if points[i][1] == points[i+1][1]:
            coord = coord + get_horizontal_line(points[i], points[i+1])
    return coord

def get_horizontal_line(p1, p2):
    p = []
    y = p1[1]
    order = 1
    if p1[0] > p2[0]:
        order = -1
    for x in range(p1[0], p2[0]+order, order):
        p.append((x,y))
    return p

def get_vertical_line(p1, p2):
    p = []
    x = p1[0]
    order = 1
    if p1[1] > p2[1]:
        order = -1
    for y in range(p1[1], p2[1]+order, order):
        p.append((x,y))
    return p

def parse_input():
    with open(INPUT_FILE_PATH) as f:
        i1 = list(map(lambda s: s.strip().split(" -> "), f.readlines()))
        return list(map(lambda l: list(map(lambda s: tuple(map(int, s.split(","))), l)), i1))

if __name__ == "__main__":
   main()