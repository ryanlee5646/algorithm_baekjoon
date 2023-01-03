from sys import stdin
from itertools import combinations
input = stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
data = [i for i in range(N)]
min_score = 1e9

rows_sum = [sum(row) for row in S]
cols_sum = [sum(col) for col in zip(*S)]
stat_by_member = [sum(x) for x in zip(rows_sum, cols_sum)]
total = sum(rows_sum)
min_score = min(abs(total - sum(stats)) for stats in combinations(stat_by_member, int(N/2)))

print(min_score)