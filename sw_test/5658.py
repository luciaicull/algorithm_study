T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = [n for n in list(input())]
    number_length = int(len(numbers) / 4)
    available_numbers = set()
    for i in range(len(numbers)):
        cur_status = numbers[-i:] + numbers[0:-i]
        for j in range(4):
            number = ''.join(cur_status[j*number_length:(j+1)*number_length])
            available_numbers.add(number)
    available_numbers = list(available_numbers)
    available_numbers.sort(reverse=True)        # (list object).sort(reverse=True): 내림차순 정렬 (default: 오름차순)
    
    K_largest = available_numbers[K-1]
    ten_digit_num = 0
    for i, n in enumerate(K_largest):
        if ord(n) >= ord('A'):                  # ord((string object)) : string(문자 하나) -> ascii code
            hex_to_dec = ord(n) - ord('A') + 10
        else:
            hex_to_dec = int(n)
        cur_number = hex_to_dec * (16 ** (len(K_largest) - 1 - i))      # ** : 제곱
        ten_digit_num += cur_number
    print('#' + str(test_case) + ' ' + str(ten_digit_num))