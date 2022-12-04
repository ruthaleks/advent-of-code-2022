INPUT_FILE_PATH = "input/d3.txt"

def main():
    input = parse_input()
    print("Part 1 = ", calc_rucksacks_priority(input))
    print("Part 2 = ", calc_rucksacks_badge_prio(input))

def calc_rucksacks_badge_prio(rucksacks):
    res = 0
    for i in range(0, len(rucksacks), 3):
        res += priority(find_common_item_type_in_group(rucksacks[i: i+3]))
    return res

def calc_rucksacks_priority(rucksacks):
    return sum(map(lambda r: priority(find_common_item_type(r)), rucksacks))

def priority(type):
    if type.isupper():
        return ord(type) - ord('A') + 27
    return ord(type) - ord('a') + 1

def find_common_item_type(input):
    first_item, second_item = items(input)
    common_type = set(first_item) & set(second_item)
    return common_type.pop()

def find_common_item_type_in_group(input):
    common_type = set(input[0]) & set(input[1]) & set(input[2])
    return common_type.pop()

def items(input):
    split_idx = len(input) // 2
    return input[0:split_idx], input[split_idx:len(input)]

def parse_input():
    with open(INPUT_FILE_PATH) as f:
        return list(map(lambda s: list(s.strip()), f.readlines()))

if __name__ == "__main__":
   main()