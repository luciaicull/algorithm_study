st = {'non_activate':0, 'activate':1, 'die':-1}
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def make_cell(item):
    return {'init_value':item, 'status':st['non_activate'], 'remaining_time':item-1}

def solution(N, M, K, initial_map):
    MAP = dict()
    # init map
    for r, row in enumerate(initial_map):
        for c, item in enumerate(row):
            if item != 0:
                MAP[(r,c)] = make_cell(item)
    # start
    for cur_time in range(K):
        cell_to_grow = dict()
        for loc in MAP.keys():
            if MAP[loc]['status'] == st['activate']:
                for dir in range(4):
                    new_loc = (loc[0]+dx[dir], loc[1]+dy[dir])
                    if new_loc not in MAP.keys():
                        if new_loc not in cell_to_grow.keys():
                            cell_to_grow[new_loc] = []
                        cell_to_grow[new_loc].append(make_cell(MAP[loc]['init_value']))
                MAP[loc]['remaining_time'] -= 1
                if MAP[loc]['remaining_time'] == 0:
                    MAP[loc]['status'] = st['die']
            elif MAP[loc]['status'] == st['non_activate']:
                if MAP[loc]['remaining_time'] == 0:
                    MAP[loc]['status'] = st['activate']
                    MAP[loc]['remaining_time'] = MAP[loc]['init_value']
                else:
                    MAP[loc]['remaining_time'] -= 1
        for loc in cell_to_grow.keys():
            if len(cell_to_grow[loc]) == 0:
                MAP[loc] = cell_to_grow[loc][0]
            else:
                max_value = max([cell['init_value'] for cell in cell_to_grow[loc]])
                MAP[loc] = make_cell(max_value)
    answer = 0
    for loc in MAP.keys():
        if MAP[loc]['status'] != st['die']:
            answer += 1
    return answer
            
T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    answer = solution(N, M, K, MAP)
    print('#{} {}'.format(test_case, answer))