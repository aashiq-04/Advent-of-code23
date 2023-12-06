with open("inp.txt","r") as file:
    data=file.read()
input_data=data.split('\n')
def is_possible(game, counts):
    for subset in game:
        cubes = subset.split('; ')
        for cube in cubes:
            colors = cube.split(', ')
            for color in colors:
                count, color_name = color.split(' ')
                if counts[color_name] < int(count):
                    return False
    return True


def possible_games(input_data, counts):
    possible = []
    
    for line in input_data:
        print(line)
        game_info = line.split(': ')
        print(game_info)
        game = game_info[1].split('; ')
        if is_possible(game, counts):
            possible.append(int(game_info[0].split(' ')[1]))
    return possible
cube_counts = {'red': 12, 'green': 13, 'blue': 14}
possible_games_list = possible_games(input_data, cube_counts)
print(sum(possible_games_list))  # Output: Sum of IDs of possible games

