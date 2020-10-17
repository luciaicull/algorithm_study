from itertools import combinations

dx = [1, 1, 1]
dy = [0, 1, -1]

def possible(loc_1, loc_2):
    if loc_1[0] != loc_2[0]:
        return True
    else:
        if abs(loc_1[1] - loc_2[1]) == 1:
            return False
        else:
            return True


def check_complete(N, H, MAP):
    for c in range(N):
        loc = (0, c)
        cur_dir = MAP[0][c]
        while loc[0] < H:
            cur_dir = MAP[loc[0]][loc[1]]
            loc = (loc[0] + dx[cur_dir], loc[1] + dy[cur_dir])
        if loc[1] != c:
            return False
    return True

def solution(N, H, MAP):
    if check_complete(N, H, MAP):
        return 0
    else:
        able_locs = []
        for x, row in enumerate(MAP):
            loc = (x, 0)
            while True:
                if loc[1] >= N-1:
                    break
                elif MAP[loc[0]][loc[1]] == 0 and MAP[loc[0]][loc[1]+1] == 0:
                    able_locs.append(loc)
                    loc = (loc[0], loc[1]+1)
                elif MAP[loc[0]][loc[1]] == 0 and MAP[loc[0]][loc[1]+1] == 1:
                    loc = (loc[0], loc[1]+3)
                elif MAP[loc[0]][loc[1]] == 1:
                    loc = (loc[0], loc[1]+2)

        # add 1
        for loc in able_locs:
            MAP[loc[0]][loc[1]] = 1
            MAP[loc[0]][loc[1]+1] = 2
            if check_complete(N, H, MAP):
                return 1
            else:
                MAP[loc[0]][loc[1]] = 0
                MAP[loc[0]][loc[1]+1] = 0

        # add 2
        for loc_list in combinations(able_locs, 2):
            if not possible(loc_list[0], loc_list[1]):
                continue
            else:
                for loc in loc_list:
                    MAP[loc[0]][loc[1]] = 1
                    MAP[loc[0]][loc[1]+1] = 2
                if check_complete(N, H, MAP):
                    return 2
                else:
                    for loc in loc_list:
                        MAP[loc[0]][loc[1]] = 0
                        MAP[loc[0]][loc[1]+1] = 0
        
        # add 3
        for loc_list in combinations(able_locs, 3):
            if not (possible(loc_list[0], loc_list[1]) and possible(loc_list[0], loc_list[2]) and possible(loc_list[2], loc_list[1])):
                continue
            else:
                for loc in loc_list:
                    MAP[loc[0]][loc[1]] = 1
                    MAP[loc[0]][loc[1]+1] = 2
                if check_complete(N, H, MAP):
                    return 3
                else:
                    for loc in loc_list:
                        MAP[loc[0]][loc[1]] = 0
                        MAP[loc[0]][loc[1]+1] = 0
                
    return -1

N, M, H = map(int, input().split())
MAP = [[0 for _ in range(N)] for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    MAP[a-1][b-1] = 1
    MAP[a-1][b] = 2
answer = solution(N, H, MAP)
print(answer)
