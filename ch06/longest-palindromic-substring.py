input_str = "babad"

# 투 포인터 확장으로 문제 접근
# expend 함수는 중첩 함수이다.


def expend(left: int, right: int) -> str:
    while left >= 0 and right < len(input_str) and input_str[left] == input_str[right]:
        print("left: ", left, "right: ", right)
        left -= 1
        right += 1
        print("left: ", left, "right: ", right)
        print("left: ", input_str[left])
        print("right: ", input_str[1:right])
        print("l + r: ", input_str[left+1:right])
    return input_str[left + 1:right]


if len(input_str) < 2 or input_str == input_str[::-1]:
    print(input_str)

result = ''

for i in range(len(input_str) - 1):
    result = max(result,
                 expend(i, i+1),
                 expend(i, i+2),
                 key=len)

print(result)