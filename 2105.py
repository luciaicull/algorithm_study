dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]
def in_field(i, j, N):
    return (i>=0 and i<N and j>=0 and j<N)

def tour(i, j, right_to_go, left_to_go, field):
    start_i, start_j = i, j
    desserts = [field[start_i][start_j]]
    cur_i, cur_j = start_i, start_j
    for dir in range(4):
        if dir%2 == 0:
            to_go = right_to_go
        else:
            to_go = left_to_go
        for _ in range(to_go):
            cur_i, cur_j = cur_i+dx[dir], cur_j+dy[dir] 
            if in_field(cur_i, cur_j, len(field)):
                if cur_i==i and cur_j==j:
                    break
                elif field[cur_i][cur_j] not in desserts:
                    desserts.append(field[cur_i][cur_j])
                else:
                    return -1
            else:
                return -1
    return len(desserts)

    
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    max_count = -1
    for i in range(0, N-2):
        for j in range(1, N-1):
            right_down_max = max(N-j-1, j)
            left_down_max = max(N-i-1, i)
            for right_to_go in range(0, right_down_max):
                for left_to_go in range(0, left_down_max):
                    count = tour(i, j, right_to_go+1, left_to_go+1, field)
                    max_count = max(max_count, count)
    print('#{} {}'.format(test_case, max_count))
