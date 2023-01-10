import collections
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

answer_str = paragraph.lower()
answer_str = re.sub('[^a-z]', ' ', answer_str)

answer_words = [word for word in answer_str.split() if word not in banned]

counts = collections.defaultdict(int)

for answer_word in answer_words:
    counts[answer_word] += 1

# print(max(counts, key=counts.get))

counts = collections.Counter(answer_words)
print(counts.most_common(1)[0][0])
