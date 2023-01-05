from sys import stdin
input = stdin.readline

N = int(input())

for _ in range(N):
    data = input().rstrip()
    if data.count('(') != data.count(')'):
      print("NO")
      continue
    stack = []
    
    for i in data:
      if i == ('('):
        stack.append(i)
      else:
        if stack:
          stack.pop()
        else:
          print("NO")
          break
    else:
      if stack:
        print("NO")
      else:
        print("YES")    
    