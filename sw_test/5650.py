# try to make code as simple as possible

dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]
directions = [[None for _ in range(4)], # dummy
          		[1, 3, 0, 2], # block 1
                [3, 0, 1, 2], # block 2
          		[2, 0, 3, 1], # block 3
                [1, 2, 3, 0], # block 4
                [1, 0, 3, 2]] # block 5

def solution(N, MAP):
    WORMHOLES = dict()
    hole_starts = [None for _ in range(5)]
    for x, row in enumerate(MAP):
        for y, num in enumerate(row):
            if num >= 6:
                if not hole_starts[num-6]:
                    hole_starts[num-6] = (x,y)
                else:
                    WORMHOLES[(x,y)] = hole_starts[num-6]
                    WORMHOLES[hole_starts[num-6]] = (x,y)
    max_score = 0   
    for start_x in range(1, N-1):
        for start_y in range(1, N-1):
            for d in range(4):
                if MAP[start_x][start_y] != 0:
                    continue
                cur_x, cur_y = start_x + dx[d], start_y + dy[d]
                cur_d = d
                score = 0
                while True:
                    if (cur_x, cur_y) == (start_x, start_y) or MAP[cur_x][cur_y] == -1:
                        break
                    elif MAP[cur_x][cur_y]  in range(1, 6):
                        cur_d = directions[MAP[cur_x][cur_y]][cur_d]
                        score += 1
                    elif MAP[cur_x][cur_y]  in range(6, 11):
                        cur_x, cur_y = WORMHOLES[(cur_x, cur_y)]
                    cur_x, cur_y = cur_x + dx[d], cur_y + dy[d]
                if score > max_score:
                    max_score = score
    return max_score           
                    
T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) + 2
    MAP = [[5] * N] + [[5] + list(map(int, input().split())) + [5] for _ in range(N-2)] + [[5] * N]
    answer = solution(N, MAP)
    print('#{} {}'.format(test_case, answer))