from sys import stdin
import sys
sys.setrecursionlimit(10000)

input = stdin.readline

# 방법 1
def josephus(arr):
  global result

  if len(arr) == 0:
    return
  
  index = K-1
  if index >= len(arr):
    index = index % len(arr)
  result.append(arr.pop(index))
  arr = arr[index:] + arr[:index]
  josephus(arr)

N, K = map(int, input().split())

data = [str(i) for i in range(1, N+1)]

result = []
josephus(data)

print("<", ', '.join(result)[:], ">", sep="")
