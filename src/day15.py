INPUT_FILE_PATH = "input/d15.txt"
import re

class Sensor:
    def __init__(self, sensor:tuple, beacon:tuple):
        self.sensor = sensor
        self.beacon = beacon
        self.distance = manhattan_distance(sensor, beacon)

    def __repr__(self):
        return ("{" + str(self.sensor) +
                "," + str(self.beacon) +
                "," + str(self.distance) +
                "}")

    def x_range(self, y:int):
        y_diff = abs(self.sensor[1] - y)
        x_min = self.sensor[0] - self.distance + y_diff
        x_max = self.sensor[0] + self.distance - y_diff
        return [(i, y) for i in range(x_min, x_max+1)]

    def x_range_limit(self, y:int, x:int):
        y_diff = abs(self.sensor[1] - y)
        x_min = self.sensor[0] - self.distance + y_diff
        x_max = self.sensor[0] + self.distance - y_diff
        if x_min >= x_max:
            return None
        return (max(0, x_min), min(x_max, x+1))

def main():
    input = parse_input()
    sensors, sb_map = setup(input)
    print("Part 1 = ", len(scan_row(sensors, sb_map)))
    print("Part 2 = ", scan_area(sensors))

def scan_area(sensors:list, max:int=4000000):
    pos = []
    for y in range(0, max+1):
        row = y
        r = scan_row_limit(sensors, row=y, xmax=max)
        if r[0][0] != 0 and r[0][1] != max:
            break
    return 4000000 * get_x_pos(r[0]) + row

def scan_row_limit(sensors:list,  row:int=2000000, xmax=4000000):
    pos = set()
    for sensor in sensors:
        xrange = sensor.x_range_limit(row, xmax)
        if xrange != None:
            pos.add(xrange)
    return merge_ranges(list(pos))

def get_x_pos(range:list):
    return range[0][1] + 1

def merge_ranges(ranges:list):
    ranges.sort()
    r1 = ranges.pop(0)
    out = []
    for r2 in ranges:
        res = merge_range(r1, r2)
        if len(res) > 1:
            out.append(res)
            r1 = res[1]
        else:
            r1 = res[0]
        out = add_to_out(r1, out)
    if len(out) == 0:
        out.append(r1)
    return out

def add_to_out(r:tuple, out:list):
    if len(out) > 0:
        last_idx = len(out)-1
        last_range = out[last_idx]
        last_range[1] = r
        out[last_idx] = last_range
        return out
    return out

def merge_range(r1:tuple, r2:tuple):
    r = [r1, r2]
    if r[1][0] <= r[0][1]:
        return [(r[0][0], max(r[1][1], r[0][1]))]
    return r

def setup(input):
    sensors = list(map(generate_sensor, input))
    sb_map = add_input_to_map(input)
    return sensors, sb_map

def scan_row(sensors:list, sb_map:dict, row:int=2000000):
    pos = set()
    for sensor in sensors:
        xrange = sensor.x_range(row)
        pos.update(list(filter(lambda x: sb_map.get(x) == None, xrange)))
    return pos

def generate_sensor(line):
    return Sensor(line[0], line[1])

def manhattan_distance(a:tuple, b:tuple):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def add_input_to_map(input):
    map = {}
    for line in input:
        sensor = line[0]
        beacon = line[1]
        map[sensor] = 'S'
        map[beacon] = 'B'
    return map


def parse_input():
    with open(INPUT_FILE_PATH) as f:
        return list(map(parse_coordinates,
            (map(lambda s: s.strip().split(" "),f.readlines()))))

def parse_coordinates(line):
    coord = list(map(to_int, [line[2], line[3], line[8], line[9]]))
    return [(coord[0], coord[1]), (coord[2], coord[3])]

def to_int(a):
    return int(re.split(r',|=|:', a)[1])

if __name__ == "__main__":
   main()
