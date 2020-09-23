delta_info = {'up':(-1,0), 'left':(0, -1), 'right':(0, 1), 'down':(1, 0)}
tunnel_type = [None, ['up', 'left', 'right', 'down'], ['up', 'down'], ['left', 'right'], ['up', 'right'], ['down', 'right'], ['down', 'left'], ['up', 'left']]
check_match = {'up':'down', 'down':'up', 'left':'right', 'right':'left'}

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tunnel_row, tunnel_col, hole_r, hole_c, L = map(int, input().split())
  
    tunnel_map = list()
    for r in range(0, tunnel_row):
        info = list(map(int, input().split()))
        tunnel_map.append(info)
    
    available_location = set()
    cur_location = [(hole_r, hole_c)]
    for _ in range(L):
        #print('cur locations : ', cur_location)
        next_locations = set()
        for loc in cur_location:
            available_location.add(loc)
            #print(loc)
            t = tunnel_map[loc[0]][loc[1]]
            #print(t)
            delta_list = tunnel_type[t]
            #print(delta_list)
            for delta in delta_list:
                x = loc[0] + delta_info[delta][0]
                y = loc[1] + delta_info[delta][1]
                if x >= 0 and x < tunnel_row and y >= 0 and y < tunnel_col:  # in map
                    if tunnel_map[x][y] != 0:  # have type
                        looking_type = tunnel_map[x][y]
                        need_delta = check_match[delta]
                        #print(looking_type, need_delta)
                        if need_delta in tunnel_type[looking_type]: # does match
                            next_locations.add((x,y))
        cur_location = next_locations

    print('#' + str(test_case) + ' ' + str(len(list(available_location))))
            

