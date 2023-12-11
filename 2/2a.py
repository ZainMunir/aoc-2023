import re
import sys


class Game:
    def __init__(self, num):
        self.num = num
        self.red = []
        self.blue = []
        self.green = []


all_games = []

for line in sys.stdin:
    print(line)
    line = line.rstrip()
    if line == "":
        break

    parts = line.split(":")
    subgames = parts[1].split(";")
    curr_game = Game(len(subgames))

    for game in subgames:
        colors = game.split(",")
        len_before = len(curr_game.green)
        for color in colors:
            color = color.strip()

            pattern = re.compile(r"\d+")
            num = pattern.search(color)
            num_col = int(num.group(0))

            if re.search("green", color):
                curr_game.green.append(num_col)
            elif re.search("red", color):
                curr_game.red.append(num_col)
            elif re.search("blue", color):
                curr_game.blue.append(num_col)
        if (len(curr_game.green) - len_before) != 1:
            curr_game.green.append(0)
        if (len(curr_game.red) - len_before) != 1:
            curr_game.red.append(0)
        if (len(curr_game.blue) - len_before) != 1:
            curr_game.blue.append(0)
    all_games.append(curr_game)

indices = []

for i, game in enumerate(all_games):
    too_large_green = list(filter(lambda x: x > 13, game.green))
    too_large_blue = list(filter(lambda x: x > 14, game.blue))
    too_large_red = list(filter(lambda x: x > 12, game.red))
    if len(too_large_green) > 0 or len(too_large_blue) > 0 or len(too_large_red) > 0:
        continue
    indices.append(i + 1)
print(sum(indices))
