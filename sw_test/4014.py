def all_same(line):
    start_item = line[0]
    for item in line:
        if item != start_item:
            return False
    return True

def enough_same_height(line_field, start_item):
    for item in line_field:
        if item != start_item:
            return False
    return True

def already_used(line_field, check_item):
    line_field.reverse()
    if line_field == []:
        return False
    for item in line_field:
        if item > check_item:
            return True
    return False

def able_to_construct(line, X):
    prev_item = line[0]
    index = 1
    while index < len(line):
        item = line[index]
        if prev_item != item:
            if abs(item - prev_item) > 1:
                return False
            else:
                if item > prev_item:
                    if index-X < 0:
                        return False
                    elif enough_same_height(line[index-X:index], prev_item):
                        if already_used(line[max(0, index-2*X):index-X], prev_item):
                            return False
                        prev_item = item
                        index += 1
                        continue
                    else:
                        return False
                else: # if item < prev_item
                    if index + X-1 >= len(line):
                        return False
                    elif enough_same_height(line[index:index+X], item):
                        prev_item = line[index+X-1]
                        index = index+X
                        continue
                    else:
                        return False
        else:
            prev_item = item
            index += 1
    return True

def solution(MAP, N, X):
    answer = 0
    # check row
    for i, row in enumerate(MAP):
        if all_same(row):
            answer += 1
        elif able_to_construct(row, X):
            answer += 1
    # check col
    for i in range(N):
        col = [MAP[r][i] for r in range(N)]
        if all_same(col):
            answer += 1
        elif able_to_construct(col, X):
            answer += 1
    return answer
    
T = int(input())

for test_case in range(1, T + 1):
    N, X = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    answer = solution(MAP, N, X)
    
    print('#{} {}'.format(test_case, answer))