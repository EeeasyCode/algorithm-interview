import collections

input_arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
sorted_str = collections.defaultdict(list)

for split_str in input_arr:
    sorted_str[''.join(sorted(split_str))].append(split_str)

print(list(sorted_str.values()))