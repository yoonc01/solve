import sys

input = sys.stdin.readline

n, m = map(int, input().split())

d = {}

for i in range(n):
    word = input().strip()
    if len(word) < m:
        continue
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1
word_list = [(-d[word], -len(word), word) for word in d]

for _, _, word in sorted(word_list):
    print(word)