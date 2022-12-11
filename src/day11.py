from functools import reduce

INPUT_FILE_PATH = "input/d11.txt"

class Monkey:
    def __init__(self, number, operation, test, items, worry_level=3):
        self.number = number
        self.item = None
        self.items = items
        self.operation = operation # ('+', int(value))
        self.test = test # (int(value), if true(#monkey), if false(#monkey))
        self.count = 0
        self.worry_level = worry_level
        self.reduction_factor = None

    def __repr__(self):
        return "{" + str(self.number) + "," + str(self.item) + "," + str(self.items) + "," + str(self.operation) + "," + str(self.test) + "}"

    def inspect_item(self):
        assert self.item == None
        if len(self.items) == 0:
            return None
        self.count += 1
        # pop first item in items list
        items = self.items
        items.reverse()
        self.item = items.pop()
        self.increse_worry_level()
        # update the items list
        items.reverse()
        self.items = items
        return self.item

    def increse_worry_level(self):
        assert self.reduction_factor != None
        op = self.operation[0]
        val = self.operation[1]
        if val == -1:
            val = self.item
        if op == '*':
            self.item = (self.item * val) % self.reduction_factor
        if op == '+':
            self.item = (self.item + val) % self.reduction_factor

    def bored(self):
        self.item = self.item // self.worry_level

    def throw(self):
        item = self.item
        self.item = None
        if item % self.test[0] == 0:
            return self.test[1], item
        return self.test[2], item

    def add_item(self, item):
        self.items.append(item)

    def set_mod_factor(self, value):
        self.reduction_factor = value

def main():
    input = parse_input()
    print("Part 1 = ", calc_monkey_business(parse_monkey_data(input), 20))
    print("Part 2 = ", calc_monkey_business(parse_monkey_data(input, 1), 10000))

def calc_monkey_business(monkeys, num_rounds):
    monkeys = run_process(monkeys, num_rounds)
    monkeys_count = list(map(lambda n: monkeys.get(n).count, monkeys.keys()))
    monkeys_count.sort(reverse=True)
    return monkeys_count[0] * monkeys_count[1]

def run_process(monkeys, num_rounds):
    for i in range(0, num_rounds):
        monkeys = simulate_round(monkeys)
    return monkeys

def simulate_round(monkeys):
    for monkey_num in monkeys.keys():
        monkey = monkeys.get(monkey_num)
        item = monkey.inspect_item()
        while item != None:
            monkey.bored()
            to_monkey, item = monkey.throw()
            monkeys.get(to_monkey).add_item(item)
            item = monkey.inspect_item()
    return monkeys

def parse_monkey_data(input, worry_level=3):
    monkeys = {}
    for i in range(0,len(input), 7):
        monkey = create_monkey(input[i:i+7], worry_level)
        monkeys[monkey.number] = monkey
    red_fact = reduce(lambda x, y: x*y, list(map(lambda n: monkeys.get(n).test[0], monkeys.keys())))
    monkeys = update_reduction_factor(monkeys, red_fact)
    return monkeys

def update_reduction_factor(monkeys, value):
    for n in monkeys.keys():
        monkey = monkeys.get(n)
        monkey.set_mod_factor(value)
    return monkeys

def create_monkey(monkey_data, worry_level=3):
    test = [0, 0, 0]
    for i in monkey_data:
        if i[0] == "Monkey":
            number = int(i[1][0])
        if i[0] == "Starting":
            items = list(map(to_int, i[2:]))
        if i[0] == "Operation:":
            val = i[5]
            if not val.isnumeric():
                val = -1
            operation = (i[4], int(val))
        if i[0] == "Test:":
            test[0] = int(i[3])
        if i[0] == "If":
            if i[1] == "true:":
                test[1] = int(i[5])
            if i[1] == "false:":
                test[2] = int(i[5])
    return Monkey(number, operation, tuple(test), items, worry_level)

def to_int(num):
    if num.isnumeric():
        return int(num)
    num = num.split(',')
    return int(num[0])

def parse_input():
    with open(INPUT_FILE_PATH) as f:
        return list(map(lambda s: s.strip().split(" "), f.readlines()))

if __name__ == "__main__":
   main()