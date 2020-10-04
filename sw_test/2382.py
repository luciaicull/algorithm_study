dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
next_direction = [2, 1, 4, 3]
def on_edge(x, N):
    if x == 0 or x == N-1:
        return True
    else:
        return False
    
def move(loc, d, N):
    direction = d-1
    x = loc[0]+dx[direction]
    y = loc[1]+dy[direction]
    if on_edge(x, N) or on_edge(y, N):
        return (x, y), next_direction[direction], True
    else:
        return (x, y), d, False
    
def solution(N, M, start_info):
    status = start_info
    #print('start')
    for time in range(M):
        #print(time)
        next_status = dict()
        for loc in status.keys():
            for group in status[loc]:
                next_loc, next_direction, die = move(loc, group['dir'], N)
                if next_loc not in next_status.keys():
                    next_status[next_loc] = []
                if die:
                    next_status[next_loc].append({'size':int(group['size']/2), 'dir':next_direction})
                else:
                    next_status[next_loc].append({'size':group['size'], 'dir':next_direction})
        for loc in next_status.keys():
            if len(next_status[loc]) > 1:
                sorted_list = sorted(next_status[loc], key=lambda group:group['size'])
                total_size = sum([group['size'] for group in next_status[loc]])
                next_dir = sorted_list[-1]['dir']
                next_status[loc] = [{'size':total_size, 'dir':next_dir}]
        status = next_status
    
    answer = 0
    for loc in status:
        answer += status[loc][0]['size']
    return answer
    
T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    start_info = dict()
    for group in range(K):
        r, c, size, direction = map(int, input().split())
        if (r,c) not in start_info.keys():
            start_info[(r,c)] = []
        start_info[(r,c)].append({'size':size, 'dir':direction})
        
    answer = solution(N, M, start_info)
    
    print('#{} {}'.format(test_case, answer))