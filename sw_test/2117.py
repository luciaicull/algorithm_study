dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def num_home(center_x, center_y, MAP, k):
    num = 0
    for delta_x in range(k):
        up_x = center_x-delta_x
        down_x = center_x+delta_x
        for y in range(center_y-k+1+delta_x, center_y+k-delta_x):
            if up_x >= 0 and up_x< len(MAP) and y >= 0 and y < len(MAP):
                num += MAP[up_x][y]
            if down_x >= 0 and down_x< len(MAP) and y >= 0 and y < len(MAP) and delta_x != 0:
                num += MAP[down_x][y]
    return num

def solution(N, M, MAP):
    max_num = -1
    for k in range(1, N+2):
        cost = k*k + (k-1)*(k-1)
        for r, row in enumerate(MAP):
            for c, home in enumerate(row):
                num = num_home(r, c, MAP, k)
                revenue = num * M
                if revenue >= cost:
                    max_num = max(max_num, num)
    return max_num
    
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    answer = solution(N, M, MAP)
    print('#{} {}'.format(test_case, answer))