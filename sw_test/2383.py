from itertools import product # 중복순열
import math

def solution(N, MAP):
    people = []
    stairs = []
    for r, row in enumerate(MAP):
        for c, num in enumerate(row):
            if num == 1:
                people.append((r, c))
            elif num >= 2:
                stairs.append({'loc':(r,c), 'length':num, 'people':[], 'arrived':[], 'leaving':[]})
    cases = list(product([i for i in range(len(stairs))], repeat=len(people)))
    min_minute = math.inf
    for case in cases:
        #init stair
        for i, stair in enumerate(stairs):
            stairs[i] = {'loc':stair['loc'], 'length':stair['length'], 'people':[], 'arrived':[], 'leaving':[]}
        for i in range(len(people)):
            p_loc = people[i]
            stair_index = case[i]
            remain = abs(p_loc[0] - stairs[stair_index]['loc'][0]) + abs(p_loc[1] - stairs[stair_index]['loc'][1])
            stairs[stair_index]['people'].append({'index':i+1, 'remain':remain})

        finished = 0
        minute = 0
        while finished < len(people):
            for stair in stairs:
                done = []
                for p_index in stair['leaving']:
                    p = [p for p in stair['people'] if p['index'] == p_index][0]
                    p['remain'] -= 1
                    if p['remain'] < -stair['length']:
                        stair['people'].remove(p)
                        finished += 1
                        done.append(p_index)
                for p_index in done:
                    stair['leaving'].remove(p_index)

                if len(stair['leaving']) < 3:
                    able_to_go = min((3 - len(stair['leaving'])), len(stair['arrived']))
                    done = []
                    for p_index in stair['arrived'][0:able_to_go]:
                        p = [p for p in stair['people'] if p['index'] == p_index][0]
                        stair['leaving'].append(p_index)
                        p['remain'] -= 1
                        done.append(p_index)
                    for p_index in done:
                        stair['arrived'].remove(p_index)


                for p in stair['people']:
                    if p['remain'] > 0:
                        p['remain'] -= 1
                    if p['remain'] == 0 and p['index'] not in stair['arrived']:
                        stair['arrived'].append(p['index'])
            minute += 1
        min_minute = min(min_minute, minute)
    return min_minute

    
                        
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    answer = solution(N, MAP)
    print('#{} {}'.format(test_case, answer))