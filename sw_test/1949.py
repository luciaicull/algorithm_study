dx = [-1,1,0,0]
dy = [0,0,-1,1]
def find_road(N, K, MAP, path):
    last_loc = path[-1]
    max_length = len(path)
    for d in range(4):
        x = last_loc[0]+dx[d]
        y = last_loc[1]+dy[d]
        if x >= 0 and x < N and y >= 0 and y < N:
            if not MAP[x][y]['used']:
                if MAP[x][y]['height'] < MAP[last_loc[0]][last_loc[1]]['height']:
                    cur_map = [[{'height':dic['height'], 'used': dic['used']} for dic in row] for row in MAP]
                    cur_map[x][y]['used'] = True 
                    length = find_road(N, K, cur_map, path+[(x,y)])
                    max_length = max(max_length, length)
                else:
                    least_to_carve = MAP[x][y]['height'] - MAP[last_loc[0]][last_loc[1]]['height'] + 1
                    if K >= least_to_carve:
                        for i in range(least_to_carve, K+1):
                            cur_map = [[{'height':dic['height'], 'used': dic['used']} for dic in row] for row in MAP]
                            cur_map[x][y]['height'] -= i
                            cur_map[x][y]['used'] = True
                            length = find_road(N, 0, cur_map, path+[(x,y)])
                            max_length = max(max_length, length)
    return max_length
    
def solve(N, K, MAP):
    max_height = 0
    for row in MAP:
        for dic in row:
            max_height = max(dic['height'], max_height)
    max_loc = []
    for r, row in enumerate(MAP):
        for c, dic in enumerate(row):
            if dic['height'] == max_height:
                max_loc.append((r,c))
    maximum_length = 0
    for loc in max_loc:
        cur_map = [[{'height':dic['height'], 'used': dic['used']} for dic in row] for row in MAP]
        cur_map[loc[0]][loc[1]]['used'] = True
        length = find_road(N, K, cur_map, [loc])
        maximum_length = max(length, maximum_length)
    return maximum_length
                
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    MAP = [[{'height':height, 'used':False} for height in list(map(int, input().split()))] for _ in range(N)]
    answer = solve(N, K, MAP)
    print('#{} {}'.format(test_case, answer))