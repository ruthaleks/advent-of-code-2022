INPUT_FILE_PATH = "input/d12.txt"
import sys

class Node:
    def __init__(self, altitude, name, coordinates, is_visited=False):
        self.altitude = altitude
        self.name = name
        self.steps_to_goal = sys.maxsize
        self.coordinates = coordinates
        self.is_visited = is_visited

    def __repr__(self):
        return ("{" + str(self.altitude) +
                "," + str(self.name) +
                "," + str(self.steps_to_goal) +
                "," + str(self.is_start) +
                "," + str(self.is_end) + "}")

    def set_steps_to_goal(self, value):
        self.steps_to_goal = min(self.steps_to_goal, value)

    def got_visited(self):
        self.is_visited = True

def main():
    map, start_node, end_node = create_map(parse_input())
    populate_steps_to_goal(map, adj_nodes(map, end_node))
    print("Part 1 = ", map.get(start_node.coordinates).steps_to_goal)
    print("Part 2 = ", find_optimal_start(map))


def find_optimal_start(node_map: dict):
    start_nodes = list(filter(lambda n: n.name == 'a', map(lambda x: node_map.get(x), node_map.keys())))
    return min(map(lambda n: n.steps_to_goal, start_nodes))



def populate_steps_to_goal(node_map, queue):
    while len(queue) > 0:
        next_node = queue.pop(0)
        next_node.got_visited()
        for n in adj_nodes(node_map, next_node):
            if n not in queue and not n.is_visited:
                queue.append(n)

def adj_nodes(map, node):
    (x, y) = node.coordinates
    return list(filter(lambda n: is_accesable_node(node, n),
                       [map.get((x+1, y)), map.get((x-1, y)),
                        map.get((x, y+1)), map.get((x, y-1))]))


def is_accesable_node(node, destination_node):
    if destination_node == None:
        return False
    if node.altitude - destination_node.altitude <= 1:
        destination_node.set_steps_to_goal(node.steps_to_goal + 1)
        return True
    return False

def create_map(input):
    map = {}
    start_node = None
    end_node = None
    for y in range(0, len(input)):
        for x in range(0, len(input[0])):
            val = input[y][x]
            if val == 'S':
                val = 'a'
                start_node = Node(ord(val), val, (x, y))
                map[(x,y)] = start_node
                continue
            elif val == 'E':
                val = 'z'
                end_node = Node(ord(val), val, (x, y), is_visited=True)
                end_node.set_steps_to_goal(0)
                map[(x,y)] = end_node
                continue
            map[(x,y)] = Node(ord(val), val, (x, y))
    return map, start_node, end_node

def parse_input():
    with open(INPUT_FILE_PATH) as f:
        return list(map(lambda s: list(s.strip()), f.readlines()))

if __name__ == "__main__":
   main()