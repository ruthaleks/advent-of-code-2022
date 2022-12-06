INPUT_FILE_PATH = "input/d6.txt"

def main():
    input = parse_input()
    print("Part 1 = ", find_first_marker(input, 4))
    print("Part 1 = ", find_first_marker(input, 14))

def find_first_marker(input, unique_markers):
    for i in range(0, len(input)-unique_markers-1):
        if len(set(input[i:i+unique_markers])) == unique_markers:
            return i+unique_markers


def parse_input():
    with open(INPUT_FILE_PATH) as f:
        return list(f.readlines()[0])

if __name__ == "__main__":
   main()