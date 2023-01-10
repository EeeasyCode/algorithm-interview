input_arr = ["h", "e", "l", "l", "o"]

# 가장 파이썬 다운 방식
# input_arr.reverse()
#
# print(input_arr)

# 투 포인터 스왑 방식
front, rear = 0, len(input_arr) - 1
while front < rear:
    input_arr[front], input_arr[rear] = input_arr[rear], input_arr[front]
    front += 1
    rear -= 1

print(input_arr)
