## A - Rock
## B - Paper
## C - Scissors

# Response
## X - Rock - lose
## Y - Paper - draw
## Z - Scissors - win

# Points
## 1 - Rock
## 2 - Paper
## 3 - Scissors
## + 0 (lost) | 3 (draw) | 6 (won)

INPUT_FILE_PATH = "input/d2.txt"
OUTCOME_SCORE_MAP = {('A', 'X'): 3,
                     ('A', 'Y'): 6,
                     ('A', 'Z'): 0,
                     ('B', 'X'): 0,
                     ('B', 'Y'): 3,
                     ('B', 'Z'): 6,
                     ('C', 'X'): 6,
                     ('C', 'Y'): 0,
                     ('C', 'Z'): 3}

INTENTION_MAP = {('A', 'X'): 'Z',
                 ('A', 'Y'): 'X',
                 ('A', 'Z'): 'Y',
                 ('B', 'X'): 'X',
                 ('B', 'Y'): 'Y',
                 ('B', 'Z'): 'Z',
                 ('C', 'X'): 'Y',
                 ('C', 'Y'): 'Z',
                 ('C', 'Z'): 'X'}


SHAPE_MAP = {'X': 1,
             'Y': 2,
             'Z': 3}

def main():
    input = parse_input()
    print("Part 1: ", total_game_score(input, False))
    print("Part 2: ", total_game_score(input, True))


def total_round_score_by_intention(input):
    return total_round_score((input[0], INTENTION_MAP.get(input)))


def total_game_score(input, intention):
    if intention:
        return sum(map(total_round_score_by_intention, input))
    return sum(map(total_round_score, input))


def total_round_score(input):
    return OUTCOME_SCORE_MAP.get(input) + SHAPE_MAP.get(input[1])


def parse_input():
    with open(INPUT_FILE_PATH) as f:
        return list(map(lambda s: tuple(s.strip().split(" ")), f.readlines()))


main()
