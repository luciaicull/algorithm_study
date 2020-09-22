delta= [(0,0), (0,-1), (1,0), (0,1), (-1,0)]

T = int(input())
for test_case in range(1, T + 1):
    M, A = map(int, input().split())  
    A_path = [0] + list(map(int, input().split()))
    B_path = [0] + list(map(int, input().split()))
    
    BC_list = []
    BC_field = dict()
    for BC_id in range(A):
        x, y, C, P = map(int, input().split())  
        print(x,y,C,P)
        for i in range(0, C+1):
            for j in range(-C+i, C+1-i):
                loc = (x+j, y-i)
                if loc not in BC_field.keys():
                    BC_field[loc] = []
                BC_field[loc].append(BC_id)
        for i in range(1, C+1):
            for j in range(-C+i, C+1-i):
                loc = (x+j, y+i)
                if loc[0] < 1 or loc[0] > 10 or loc[1] < 1 or loc[1] > 10:
                    continue
                if loc not in BC_field:
                    BC_field[loc] = []
                BC_field[loc].append(BC_id)
    
    
    A_loc = (1,1)
    B_loc = (10,10)
    a_sum, b_sum = 0, 0
    result = 0
    for mov_a, mov_b in zip(A_path, B_path):
        A_loc = (A_loc[0] + delta[mov_a][0], A_loc[1] + delta[mov_a][1])
        B_loc = (B_loc[0] + delta[mov_b][0], B_loc[1] + delta[mov_b][1])
        if (A_loc in BC_field.keys()) and (B_loc not in BC_field.keys()):
            result += max([BC_list[index] for index in BC_field[A_loc]])
        elif (A_loc not in BC_field.keys()) and (B_loc in BC_field.keys()):
            result += max([BC_list[index] for index in BC_field[B_loc]])
        elif (A_loc in BC_field.keys()) and (B_loc in BC_field.keys()):
            tmp_max = 0
            for BC_a_id in BC_field[A_loc]:
                for BC_b_id in BC_field[B_loc]:
                    if BC_a_id == BC_b_id:
                        tmp_sum = BC_list[BC_a_id]
                    else:
                        tmp_sum = BC_list[BC_a_id] + BC_list[BC_b_id]
                    if tmp_sum > tmp_max:
                        tmp_max = tmp_sum
            result += tmp_max
    print('#' + str(test_case) + ' ' + str(int(result)))