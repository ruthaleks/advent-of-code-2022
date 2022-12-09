INPUT_FILE_PATH = "input/d9.txt"

DIR_MAP = {"R": ( 1, 0),
           "L": (-1, 0),
           "U": ( 0, 1),
           "D": ( 0,-1)}

def main():
    input = parse_input()
    print("Part 1 =", simulate(input, 2))
    print("Part 2 =", simulate(input, 10))

def simulate(input, knots):
    cmds = list(map(parse_cmd, input))
    tail_visits = set()
    start = (0, 0)
    rope = [start for i in range(0, knots)]
    tail_visits.add(start)
    cmd = cmds[0]
    for cmd in cmds:
        (dir, steps) = cmd
        for step in range(0, steps):
            rope[0] = move_head(rope[0], dir)
            for i in range(0, knots-1):
                rope[i+1] = adjust_tail(rope[i], rope[i+1])
            tail_visits.add(rope[-1])
    return len(tail_visits)

def parse_cmd(cmd):
    l = cmd.split(" ")
    return l[0], int(l[1])

def move_head(head, dir):
    return add_tuples(head, DIR_MAP.get(dir))

def adjust_tail(head, tail):
    if is_tail_touching(head, tail):
        return tail
    new_tail = add_tuples(tail, tail_move(head, tail))
    return new_tail

def tail_move(head, tail):
    # (x, y)
    #(-1, 1)(0, 1)(1, 1)
    #(-1, 0)(0, 0)(1, 0)
    #(-1,-1)(0,-1)(1,-1)
    diagonal_moves = [( 1,-1),
                      (-1, 1),
                      ( 1, 1),
                      (-1,-1)]
    moves = [( 0, 1),
             (-1, 0),
             ( 1, 0),
             ( 0,-1)]
    alloved_moves = moves
    if not tail_in_same_row_or_col(head, tail):
        alloved_moves = diagonal_moves

    for move in alloved_moves:
        new_tail = add_tuples(tail, move)
        if is_tail_touching(head, new_tail):
            return move

def tail_in_same_row_or_col(head, tail):
    return head[0] == tail[0] or head[1] == tail[1]

def add_tuples(a, b):
    return(a[0]+b[0], a[1]+b[1])

def is_tail_touching(head, tail):
    head_x, head_y = head
    tail_x, tail_y = tail
    return abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1

def parse_input():
    with open(INPUT_FILE_PATH) as f:
        return list(map(lambda s: s.strip(), f.readlines()))

if __name__ == "__main__":
   main()