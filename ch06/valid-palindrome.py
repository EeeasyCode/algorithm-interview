import re

test_input = "A man, a plan, a canal: Panama"

answer_str = test_input.lower()

answer_str = re.sub('[^a-z0-9]', '', answer_str)

if answer_str == answer_str[::-1]:
    print("True")
    print(answer_str)
    print(answer_str[::-1])

else:
    print("False")

