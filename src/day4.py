
INPUT_FILE_PATH = "input/d4.txt"

def main():
    input = parse_input()
    print("Part 1 = ", assignment_check(input, False))
    print("Part 2 = ", assignment_check(input, True))

def assignment_check(assignments, check_part_overlap):
    return sum(map(lambda a: overlap(to_int_range(a), check_part_overlap), assignments))

def overlap(input, check_part_overlap):
    first_section = set(input[0])
    second_section = set(input[1])
    overlap = first_section & second_section
    if check_part_overlap and len(overlap) > 0:
        return 1
    if overlap == first_section or overlap == second_section:
        return 1
    return 0

def to_int_range(input):
    return list(map(lambda s: to_range(list(map(int, s.split("-")))), input))

def to_range(input):
    return [i for i in range(input[0], input[1]+1)]

def parse_input():
    with open(INPUT_FILE_PATH) as f:
        return list(map(lambda s: s.strip().split(","), f.readlines()))

if __name__ == "__main__":
   main()