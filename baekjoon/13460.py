dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move_ball(loc_dict, direction, EMPTY_MAP):
    next_loc_dict = {'R': None, 'B': None}
    hole_in = False
    for key in loc_dict.keys():
        cur_loc = [loc_dict[key][0], loc_dict[key][1]]
        next_loc = [cur_loc[0]+dx[direction], cur_loc[1]+dy[direction]]
        while True:
            if EMPTY_MAP[next_loc[0]][next_loc[1]] == '.':
                cur_loc = next_loc
                next_loc = [cur_loc[0]+dx[direction], cur_loc[1]+dy[direction]]
            elif EMPTY_MAP[next_loc[0]][next_loc[1]] == 'O':
                cur_loc = next_loc
                hole_in = True
                break
            elif EMPTY_MAP[next_loc[0]][next_loc[1]] == '#':
                break
        next_loc_dict[key] = cur_loc
    
    if next_loc_dict['R'] == next_loc_dict['B'] and not hole_in:
        if direction == 0: # up
            if loc_dict['R'][0] < loc_dict['B'][0]:
                next_loc_dict['B'][0] += 1
            else:
                next_loc_dict['R'][0] += 1
        elif direction == 1: # down
            if loc_dict['R'][0] < loc_dict['B'][0]:
                next_loc_dict['R'][0] -= 1
            else:
                next_loc_dict['B'][0] -= 1
        elif direction == 2: # left
            if loc_dict['R'][1] < loc_dict['B'][1]:
                next_loc_dict['B'][1] += 1
            else:
                next_loc_dict['R'][1] += 1
        elif direction == 3: # right
            if loc_dict['R'][1] < loc_dict['B'][1]:
                next_loc_dict['R'][1] -= 1
            else:
                next_loc_dict['B'][1] -= 1
    return next_loc_dict


def solution(N, M, RAW_MAP):
    cur_level_locs = []
    loc = dict()
    EMPTY_MAP = [[None for _ in range(M)] for _ in range(N)]
    for x, row in enumerate(RAW_MAP):
        for y, item in enumerate(row):
            if item == 'R' or item == 'B':
                loc[item] = [x,y]
                EMPTY_MAP[x][y] = '.'
            else:
                EMPTY_MAP[x][y] = item
    cur_level_locs.append(loc)

    count = 1
    while count <= 10:
        next_level_locs = []
        for loc_dict in cur_level_locs:
            for direction in range(4):
                next_loc_dict = move_ball(loc_dict, direction, EMPTY_MAP)
                if EMPTY_MAP[next_loc_dict['R'][0]][next_loc_dict['R'][1]] == 'O' and EMPTY_MAP[next_loc_dict['B'][0]][next_loc_dict['B'][1]] == 'O':
                    continue
                elif EMPTY_MAP[next_loc_dict['R'][0]][next_loc_dict['R'][1]] != 'O' and EMPTY_MAP[next_loc_dict['B'][0]][next_loc_dict['B'][1]] == 'O':
                    continue
                elif EMPTY_MAP[next_loc_dict['R'][0]][next_loc_dict['R'][1]] == 'O' and EMPTY_MAP[next_loc_dict['B'][0]][next_loc_dict['B'][1]] != 'O':
                    return count
                elif next_loc_dict['R'] == loc_dict['R'] and next_loc_dict['B'] == loc_dict['B']:
                    continue
                else:
                    next_level_locs.append(next_loc_dict)
        
        if len(next_level_locs) == 0:
            return -1

        cur_level_locs = next_level_locs
        count += 1
    
    return -1


N, M = map(int, input().split())
RAW_MAP = [list(input()) for _ in range(N)]
answer = solution(N, M, RAW_MAP)
print(answer)