from sys import stdin
from itertools import *
input = stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))

result = sorted(set(list(combinations_with_replacement(sorted(data), M))))
for i in result:
    print(*i)