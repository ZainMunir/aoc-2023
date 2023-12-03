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

powers = []

for game in all_games:
    max_green = max(game.green)
    max_blue = max(game.blue)
    max_red = max(game.red)
    powers.append(max_green * max_blue * max_red)
print(sum(powers))
