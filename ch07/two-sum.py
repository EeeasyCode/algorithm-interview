num = [2, 7, 11, 15]
target = 9

# 1 브루트 포스로 계산

for i in range(len(num)):
    for j in range(i+1, len(num)):
        if num[i] + num[j] == target:
            print(i, j)

# 2 in을 이용한 탐색

for i, n in enumerate(num):
    complement = target - n

    if complement in num[i+1:]:
        print(num.index(n), num[i+1:].index(complement) + (i+1))

# 3 첫 번째 수를 뺀 결과 키 조회

num_map = {}

for i, num_int in enumerate(num):
    num_map[num_int] = i

for i, num_int in enumerate(num):
    if target - num_int in num_map and i != num_map[target-num_int]:
        print([i, num_map[target-num_int]])

# 4 조회 구조 개선

num_map = {}

for i, num_int in enumerate(num):
    if target - num_int in num_map:
        print([num_map[target - num_int], i])
    num_map[num_int] = i