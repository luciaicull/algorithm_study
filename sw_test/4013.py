LEFT_FACING_INDEX = 6
RIGHT_FACING_INDEX = 2
SCORE_INDEX = 0
def check_left_magnetic(direction, status, cur_index):
    if status[cur_index][LEFT_FACING_INDEX] != status[cur_index-1][RIGHT_FACING_INDEX]:
        if cur_index - 1 > 0:
            status = check_left_magnetic(direction * (-1), status, cur_index-1)
        status[cur_index-1] = turn_magnetic(status[cur_index-1], direction * (-1))
    return status

def check_right_magnetic(direction, status, cur_index):
    if status[cur_index][RIGHT_FACING_INDEX] != status[cur_index+1][LEFT_FACING_INDEX]:
        if cur_index + 1 < 3:
            status = check_right_magnetic(direction * (-1), status, cur_index+1)
        status[cur_index+1] = turn_magnetic(status[cur_index+1], direction * (-1))
    return status

def turn_magnetic(cur_status, direction):
    if direction == 1:
        changed_status = [cur_status[-1]] + cur_status[:-1]
    else:
        changed_status = cur_status[1:] + [cur_status[0]]
    return changed_status

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    k = int(input())
    
    # get current magnetic status
    status = []
    for _ in range(4):
        magnetic = input().split(' ')
        magnetic = [int(m) for m in magnetic]
        status.append(magnetic)
        
    # problem solving    
    for _ in range(k):
        magnetic_num,  direction =  map(int, input().split())
        if magnetic_num-1 != 0:
        	status = check_left_magnetic(direction, status, magnetic_num-1)
        if magnetic_num-1 != 3:
       	 	status = check_right_magnetic(direction, status, magnetic_num-1)

        status[magnetic_num-1] = turn_magnetic(status[magnetic_num-1], direction)
                            
    # calculate score
    score = 0
    for i, st in enumerate(status):
        score += st[SCORE_INDEX]*(2**i)
        
    print('#'+str(test_case)+' ' + str(score))