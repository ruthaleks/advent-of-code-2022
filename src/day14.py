INPUT_FILE_PATH = "input/d14s1.txt"

import sys

def main():
    input = parse_input()
    print("Part 1 = ", simulation(input))
    print("Part 2 = ", simulation_with_floor(input))

def simulation(input:list):
    grid = create_grid(input)
    units = 0
    cont = True
    while cont:
        cont = add_one_unit_sand(grid)
        units += 1
    #print_grid(input, grid)
    return units-1

def simulation_with_floor(input:list):
    grid = create_grid(input)
    add_floor(input, grid)
    print_grid(input, grid)
    cont = True
    units = 0
    while grid.get((500, 0)) == '.':
        cont = add_one_unit_sand(grid)
        units += 1
    #print_grid(input, grid)
    return units

def add_one_unit_sand(grid):
    source = (500, 0)
    current = source
    cont = True
    while cont:
        current, cont = get_next_pos(current, grid)
    if current != None:
        assert grid.get(current) == '.'
        grid[current] = 'o'
    return current != None

def get_next_pos(current:tuple, grid:dict):
    (x, y) = current
    next = (x, y+1)
    if grid.get(next) == None:
        return None, False
    if grid.get(next) == '.':
        return next, True
    if grid.get(next) == '#' or grid.get(next) == 'o':
        # try go to left
        left = (x-1, y+1)
        if grid.get(left) == '#' or grid.get(left) == 'o':
            #try to go right
            right = (x+1, y+1)
            if grid.get(right) == '#' or grid.get(right) == 'o':
                return current, False
            else:
                return right, True
        else:
            return left, True

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

    return x_max, x_min, y_max+2

def create_grid(input:list):
    x_max, x_min, y_max = grid_size(input)
    lines = [item for sublist in list(map(get_lines, input)) for item in sublist]
    grid = {}
    for y in range(0, y_max+1):
        for x in range(x_min, x_max+1):
            if (x,y) in lines:
                grid[(x,y)] = '#'
            else:
                grid[(x,y)] = '.'
    return grid

def add_floor(input:list, grid:dict):
    x_max, x_min, y_max = grid_size(input)
    for x in range(x_min, x_max+1):
        grid[(x,y_max)] = '#'
    return grid

def print_grid(input:list, grind:dict):
    x_max, x_min, y_max = grid_size(input)
    for y in range(0, y_max+1):
        row = ""
        for x in range(x_min, x_max+1):
            row = row + grind.get((x,y))
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