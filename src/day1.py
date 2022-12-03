
INPUT_FILE_PATH = "input/d1.txt"

def main():
    calories = parse_input()
    print("Part 1 = ", max_total_calories(calories))
    print("Part 2 = ", max_top_three_total_calories(calories))


def parse_input():
    with open(INPUT_FILE_PATH) as f:
        return list(map(lambda s: list(map(int, s.split("\n"))), ''.join(f.readlines()).split("\n\n")))

def max_total_calories(calories):
    return max(map(sum, calories))

def max_top_three_total_calories(calories):
    return sum(sorted(list(map(sum, calories)))[::-1][0:3])

main()