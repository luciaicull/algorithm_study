# 초기화에 신경쓸 것
import math

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def find_top_indices(width, height, block_map):
    top_indices = []
    for w in range(width):
        col = [block_map[h][w] for h in range(height)]
        for i, item in enumerate(col):
            if item != 0:
                top_indices.append((i, w))
                break
    return top_indices

def count_remain(block_map):
    count = 0
    for row in block_map:
        for item in row:
            if item != 0:
                count += 1
    return count

def empty_map(block_map):
    for row in block_map:
        for item in row:
            if item != 0:
                return False
    return True

def add_new_bombs(w, h, block_map, loc, new_bombs):
    bomb_range = block_map[loc[0]][loc[1]]
    for d in range(4):
        for br in range(1, bomb_range):
            x = loc[0] + dx[d]*br
            y = loc[1] + dy[d]*br
            if x>=0 and x<h and y>=0 and y<w:
                if block_map[x][y] > 1:
                    new_bombs.add((x,y))
    return new_bombs

def explode(w, h, block_map, top_loc):
    cur_map = [[block_map[r][c] for c in range(w)] for r in range(h)]
    used_bombs = set()
    bomb_locs_to_check = [top_loc]
    while bomb_locs_to_check != []:
        new_bombs = set()
        for loc in bomb_locs_to_check:
            if loc not in list(used_bombs):
                used_bombs.add(loc)
                new_bombs = add_new_bombs(w, h, cur_map, loc, new_bombs)
        bomb_locs_to_check = list(new_bombs)

    used_bombs = list(used_bombs)
    for loc in used_bombs:
        bomb_range = cur_map[loc[0]][loc[1]]
        for d in range(4):
            for br in range(1, bomb_range):
                x = loc[0] + dx[d]*br
                y = loc[1] + dy[d]*br
                if x>=0 and x<h and y>=0 and y<w and (x,y) not in used_bombs:
                    cur_map[x][y] = 0
    for loc in used_bombs:
        cur_map[loc[0]][loc[1]] = 0

    return cur_map

def down_blocks(width, height, block_map):
    cur_map = [[block_map[h][w] for w in range(width)] for h in range(height)]
    for w in range(width):
        column = [block_map[h][w] for h in range(height)]
        new_col = []
        for item in column:
            if item == 0:
                new_col = [item] + new_col
            else:
                new_col = new_col + [item]
        for h in range(height):
            cur_map[h][w] = new_col[h]
    return cur_map


def solution(n, w, h, block_map):
    if n == 0 or empty_map(block_map):
        remaining_blocks = count_remain(block_map)
        return remaining_blocks

    top_indices = find_top_indices(w, h, block_map)
    min_blocks = math.inf
    for top_loc in top_indices:
        cur_map = [[block_map[r][c] for c in range(w)] for r in range(h)]
        exploded_map = explode(w, h, cur_map, top_loc)
        exploded_map = down_blocks(w, h, exploded_map)

        remaining_blocks = solution(n-1, w, h, exploded_map)
        min_blocks = min(remaining_blocks, min_blocks)
    return min_blocks


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(H)]

    answer = solution(N, W, H, MAP)
    print('#{} {}'.format(test_case, answer))
