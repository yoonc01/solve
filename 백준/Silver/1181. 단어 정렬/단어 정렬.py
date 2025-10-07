import sys
input = sys.stdin.readline

n = int(input())

words = set()

for _ in range(n):
    word = input().strip()
    words.add(word)

word_list = sorted(words, key=lambda x: (len(x), x))

for word in word_list:
    print(word)
