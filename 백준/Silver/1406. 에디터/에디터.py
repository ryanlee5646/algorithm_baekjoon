from sys import stdin
input = stdin.readline


words = list(input().strip())
N = int(input())

right = []

for i in range(N):

  command = input().rstrip().replace(" ", "")
  
  if command[0] == "L":
    if words:
      right.append(words.pop())
      
  elif command[0] == "D":
    if right:
      words.append(right.pop())
      
  elif command[0] == "B":
    if words:
      words.pop()
      
  elif command[0] == "P":
      words.append(command[1])

print(''.join(words + list(reversed(right))))