INPUT_FILE_PATH = "input/d13.txt"
import functools
def main():
    input = parse_input()
    print("Part 1 = ", calc_sum_of_idx(input))
    print("Part 2 = ", find_div_packets(input))

def find_div_packets(input:list):
    div1 = [[2]]
    div2 = [[6]]
    input = input + [div1, div2]
    input.sort(key=functools.cmp_to_key(comp), reverse=True)
    return (input.index(div1)+1) * (input.index(div2)+1)

def calc_sum_of_idx(input):
    idx = 1
    right_order_idx = []
    for i in range(0, len(input), 2):
        is_right_order = comp(input[i], input[i+1])
        if is_right_order != -1:
            right_order_idx.append(idx)
        idx += 1
    return sum(right_order_idx)

def comp(pair1, pair2):
    for i in range(0, len(pair1)):
        if i > len(pair2) - 1:
            return -1
        if type(pair1[i]) is list or type(pair2[i]) is list:
            cmp_res = comp(to_list(pair1[i]), to_list(pair2[i]))
            if cmp_res != 0:
                return cmp_res
        elif pair1[i] < pair2[i]:
            return 1
        elif pair1[i] > pair2[i]:
            return -1

    if len(pair2) > len(pair1):
        return 1
    return 0

def to_list(val):
    if type(val) is list:
        return val
    return [val]

def parse_input():
    with open(INPUT_FILE_PATH) as f:
        return list(map(eval, filter(lambda x: x != '', map(lambda s: s.strip(), f.readlines()))))

if __name__ == "__main__":
   main()