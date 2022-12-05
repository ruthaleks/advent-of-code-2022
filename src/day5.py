INPUT_FILE_PATH = "input/d5.txt"

SACS = {}

def main():
    input = parse_input()
    move_cmds = setup_map(input)
    print("Part 1 = ", get_top_crates(move_cmds, apply_move_cmd_cranemover9000))
    setup_map(input)
    print("Part 2 = ", get_top_crates(move_cmds, apply_move_cmd_cranemover9001))

def setup_map(input):
    SACS = {}
    idx = split_idx(input)
    parse_crates(input[0:idx][::-1])
    return parse_move_cmds(input[idx+2:len(input)])


def get_top_crates(cmds, crane_func):
    list(map(crane_func, cmds))

    return ''.join(list(map(lambda key: SACS.get(key)[-1], SACS.keys())))

def apply_move_cmd_cranemover9001(cmd):
    amount = cmd[0]
    from_crate = cmd[1]
    to_crate = cmd[2]
    source_crate = list(SACS.get(from_crate))
    dest_crate = list(SACS.get(to_crate))
    cargo = source_crate[-amount:len(source_crate)]
    for i in range(0, amount):
        source_crate.pop()
    SACS[from_crate] = source_crate
    SACS[to_crate] = dest_crate + cargo

def apply_move_cmd_cranemover9000(cmd):
    amount = cmd[0]
    from_crate = cmd[1]
    to_crate = cmd[2]
    source_crate = list(SACS.get(from_crate))
    dest_crate = list(SACS.get(to_crate))
    for i in range(0, amount):
        dest_crate.append(source_crate.pop())
    SACS[from_crate] = source_crate
    SACS[to_crate] = dest_crate

def arrage_crates(line):
    sack = 1
    for i in range(0, len(line), 4):
        if line[i] == "[":
            if sack in SACS.keys():
                s = list(SACS.get(sack))
                s.append(line[i+1])
                SACS[sack] = s
            else:
                SACS[sack] = [line[i+1]]
        sack += 1
    return 0

def split_idx(input):
    idx = 0
    for i in input:
        if i[0:2] == " 1":
            return idx
        idx += 1

def parse_move_cmds(input):
    l = list(map(lambda sublist: list(map(lambda s: s.strip(), sublist.split(" "))), input))
    str_l = list(map(lambda sublist: list(filter(lambda s: s.isnumeric(), sublist)),l))
    return(list(map(lambda sublist: list(map(int, sublist)), str_l)))

def parse_crates(input):
    list(map(lambda i: arrage_crates(list(i)), input))

def parse_input():
    with open(INPUT_FILE_PATH) as f:
        return f.readlines()

if __name__ == "__main__":
   main()