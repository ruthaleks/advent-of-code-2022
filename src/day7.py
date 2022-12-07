INPUT_FILE_PATH = "input/d7.txt"
EXECUTION_TAG = "$"
CHANGE_DIR = "cd"
LIST = "ls"
DIR = "dir"


class Node:
    def __init__(self, name, parent=None, size=0):
        self.name = name
        self.size = size
        self.subdirs = []
        self.subfiles = []
        self.parent = parent

    def __repr__(self):
        return "name = " + self.name + " size = " + str(self.size)

    def add_file(self, name, size):
        parent = self
        while parent is not None:
            parent.size += size
            parent = parent.parent
        self.subfiles.append(Node(name, self, size))

    def add_dir(self, name):
        self.subdirs.append(Node(name, self))

    def change_dir(self, name):
        if name == '..':
            return self.parent
        for node in self.subdirs:
            if node.name == name:
                return node
        if self.name == name:
            return self


def all_dirs(nodes, dirs):
    if nodes == []:
        return dirs
    n = nodes.pop()
    for node in n.subdirs:
        if node not in nodes:
            nodes.append(node)
        if node not in dirs:
            dirs.append(node)
    return all_dirs(nodes, dirs)

def main():
    input = parse_input()
    print("Part 1 = ", calc_total_size(input, 100000))
    print("Part 2 = ", size_of_deleted_dir(input))

def size_of_deleted_dir(input):
    root = create_tree(input)
    dirs = all_dirs([root], []) + [root]
    unused_space = 70000000 - root.size
    req_space = 30000000 - unused_space
    lim_dirs = list(filter(lambda d: d.size >= req_space, dirs))
    return sorted(map(lambda d: d.size, lim_dirs))[0]


def calc_total_size(input, limit):
    root = create_tree(input)
    dirs = all_dirs([root], []) + [root]
    lim_dirs = list(filter(lambda d: d.size < limit, dirs))
    return sum(map(lambda d: d.size, lim_dirs))

def create_tree(input):
    root = Node("/")
    node = root
    for line in input:
        node = execute_line(line, node)
    return root

def execute_line(line, node):
    cmd = line.split(" ")
    if cmd[0] == EXECUTION_TAG:
        if cmd[1] == CHANGE_DIR:
            node = node.change_dir(cmd[2])
        elif cmd[1] == LIST:
            pass
    elif cmd[0] == DIR:
        node.add_dir(cmd[1])
    elif cmd[0].isnumeric():
        node.add_file(cmd[1], int(cmd[0]))
    return node

def parse_input():
    with open(INPUT_FILE_PATH) as f:
        return list(map(lambda s: s.strip(), f.readlines()))

if __name__ == "__main__":
   main()