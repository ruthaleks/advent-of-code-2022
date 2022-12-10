INPUT_FILE_PATH = "input/d10.txt"

CYCLE_MAP = {"noop": 1,
             "addx": 2}

def main():
    input = parse_input()
    print("Part 1 = ", run_program(input))
    ctr = write_on_ctr(create_empty_ctr((40, 6)), input)
    print("Part 2 = ")
    print_ctr(ctr, (40, 6))

def write_on_ctr(ctr, indata):
    X = 1
    coordinates = ctr.keys()
    cmds = list(map(create_cmd, indata))
    cmds.reverse()
    current_cmd = cmds.pop()
    for c in coordinates:
        if in_range(X, c):
            ctr[c] = '#'
        else:
            ctr[c] = ' '
        X, change_cmd, current_cmd = update_X(X, current_cmd)
        if change_cmd and len(cmds) > 0:
            current_cmd = cmds.pop()
    return ctr

def create_cmd(line):
    value = 0
    if len(line) > 1:
        value = int(line[1])
    return (line[0], value, 1)

def update_X(X, cmd):
    (c, v, t) = cmd
    if t == CYCLE_MAP.get(c):
        return X+v, True, cmd
    return X, False, (c, v, t+1)

def in_range(X, coord):
    return coord[0] in get_stripe(X)

def get_stripe(X):
    return (X-1, X, X+1)

def create_empty_ctr(dim):
    ctr = {}
    (x_max, y_max) = dim
    for y in range(0, y_max):
        for x in range(0, x_max):
            ctr[(x,y)] = '*'
    return ctr

def print_ctr(ctr, dim):
    (x_max, y_max) = dim
    for y in range(0, y_max):
        line = ""
        for x in range(0, x_max):
            line += ctr.get((x,y))
        print(line)

def run_program(input):
    signals = [(i, 0) for i in range(20, 221, 40)]
    X = (1, 1)
    for cmd in input:
        X, signals = exec_cmd(X, cmd, signals)
    return sum(map(lambda x: x[1], signals))

def exec_cmd(X, cmd, signals):
    (X_signal, X_cycle) = X
    cycles = CYCLE_MAP.get(cmd[0])
    value = 0
    if len(cmd) > 1:
        value = int(cmd[1])
    for i in range(0, cycles-1):
        X_cycle += 1
        signals = update_signal_strength((X_signal, X_cycle), signals)
    X_cycle += 1
    X_signal += value
    signals = update_signal_strength((X_signal, X_cycle), signals)
    return (X_signal, X_cycle), signals

def update_signal_strength(X, signals):
    (X_signal, X_cycle) = X
    time = list(map(lambda x: x[0], signals))
    if X_cycle not in time:
        return signals
    idx = time.index(X_cycle)
    el = signals[idx]
    signals[idx] = (el[0], X_signal*el[0])
    return signals

def parse_input():
    with open(INPUT_FILE_PATH) as f:
        return list(map(lambda s: s.strip().split(" "), f.readlines()))

if __name__ == "__main__":
   main()
