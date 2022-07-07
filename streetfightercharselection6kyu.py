# %%
# Forfieted
# %%
# sol 1


MOVES = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}


def street_fighter_selection(fighters, initial_position, moves):
    y, x = initial_position
    hovered_fighters = []
    for move in moves:
        dy, dx = MOVES[move]
        y += dy
        if not 0 <= y < len(fighters):
            y -= dy
        x = (x + dx) % len(fighters[y])
        hovered_fighters.append(fighters[y][x])
    return hovered_fighters
# %%
# sol 2 easy sol


def street_fighter_selection(fighters, initial_position, moves):
    cur_pos = [initial_position[0], initial_position[1]]
    selected_fighters = []

    for move in moves:
        if move == "up":
            cur_pos[0] = 0
        elif move == "down":
            cur_pos[0] = 1
        elif move == "right":
            cur_pos[1] = (cur_pos[1] + 1) % 6
        elif move == "left":
            cur_pos[1] = (cur_pos[1] - 1) % 6
        selected_fighters.append(fighters[cur_pos[0]][cur_pos[1]])

    return selected_fighters
# %%
# sol 3


def street_fighter_selection(fighters, initial_position, moves):
    x, y = initial_position
    fighter_list = []

    options = {
        'up': lambda y: y - 1 if y != 0 else 0,
        'down': lambda y: y + 1 if y != 1 else 1,
        'left': lambda x: x - 1 if x != 0 else 5,
        'right': lambda x: x + 1 if x != 5 else 0}

    for move in moves:
        if move == 'up' or move == 'down':
            y = options[move](y)
        else:
            x = options[move](x)
        fighter_list.append(fighters[y][x])

    return fighter_list
