from sys import stdin
input = stdin.readline

N = int(input())

for _ in range(N):
  data = list(input().split())
  
  result = ""
  
  for i in data:
    result += i[::-1]
    result += " "
  print(result)