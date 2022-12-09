INPUT_FILE_PATH = "input/d8.txt"

ABOVE = (0, -1)
BELOW = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

def main():
    rows, cols, input = parse_input()
    map = create_map(input)
    count, score = count_visable(rows, cols, map)
    print("Part 1 = ", count)
    print("Part 2 = ", score)

def count_visable(rows, cols, map):
    count = 0
    scores = []
    for y in range(0, rows):
        for x in range(0, cols):
            c = (x, y)
            h = map.get(c)
            a, sa = is_visable(h, c, ABOVE, map, rows, cols, 0)
            b, sb = is_visable(h, c, BELOW, map, rows, cols, 0)
            r, sr = is_visable(h, c, RIGHT, map, rows, cols, 0)
            l, sl = is_visable(h, c, LEFT, map, rows, cols, 0)
            scores.append(sa * sb * sr * sl)
            if a or b or r or l:
                count += 1
    return count, max(scores)

def is_visable(height, cord, diff, map, rows, cols, score):
    (x, y) = cord
    (dx, dy) = diff
    if is_edge(x, y, cols-1, rows-1):
        return True, score
    if height > map.get((x+dx, y+dy)):
        return is_visable(height, (x+dx, y+dy), diff, map, rows, cols, score+1)
    return False, score + 1

def is_edge(x, y, x_max, y_max):
    return x == 0 or x == x_max or y == 0 or y == y_max

def create_map(input):
    # x increasing from left to right
    # y increasing from top to bottom
    x = 0
    y = 0
    map = {}
    for row in input:
        for tree in row:
            map[(x, y)] = int(tree)
            x += 1
        y += 1
        x = 0
    return map


def parse_input():
    with open(INPUT_FILE_PATH) as f:
        input = list(map(lambda s: s.strip(), f.readlines()))
        rows = len(input)
        cols = len(list(input[0]))
        return rows, cols, input

if __name__ == "__main__":
   main()