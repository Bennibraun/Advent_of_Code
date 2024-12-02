
f = open('advent2.txt','r')

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

games = {}
for g in f.readlines():
    id = int(g.split(' ')[1].replace(':',''))
    games[id] = {}
    game = g.split(':')[-1].strip()
    for isub,subset in enumerate(game.split(';')):
        subset = subset.strip()
        # 6 red, 1 blue, 3 green
        colors = {}
        for item in subset.split(','):
            num,col = item.strip().split(' ')
            colors[col] = int(num)
        games[id][isub] = colors

# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
limits = {'red':12,'green':13,'blue':14}

valid_games_id_sum = 0

def is_valid(game,limits):
    for subset in game.values():
        for col,val in subset.items():
            if val > limits[col]:
                return False
    return True

for id,game in games.items():
    if is_valid(game,limits):
        valid_games_id_sum += id

print(valid_games_id_sum)


# Part 2
# For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?

def min_cubes_power(game):
    mins = {'red':0,'green':0,'blue':0}
    for subset in game.values():
        for col,val in subset.items():
            mins[col] = max(mins[col],int(val))
    
    return mins['red'] * mins['green'] * mins['blue']


power_sum = 0
for id,game in games.items():
    power_sum += min_cubes_power(game)

print(power_sum)