from sys import stdin
input = stdin.readline

S = list(input().rstrip())

stack = []

tag_yn = False

result = ""

for i in S:
  if i == "<": # 태그 시작이면 태그유무 flag = True 하고 문자열에 바로 추가해줌
    if stack:
      N = len(stack)
      for _ in range(N):
        result += stack.pop()
    tag_yn = True
    result += i
  elif i == ">": # 태그 종료면 태그유무 flag = False하고 문자열에 바로 추가해줌
    tag_yn = False
    result += i
  else: # 일반문자열이면서 
    if tag_yn: # 태그에 해당하면 문자열 추가 
      result += i 
    else: # 태그가 아니고
      if i == " ": # 공백이면 스택에 있는 문자 출력 후 공백추가
        N = len(stack)
        for _ in range(N):
            result += stack.pop()
        result += " "
      else: # 공백이 아니라면 stack에 추가
        stack.append(i)
      
if stack:
  N = len(stack)
  for _ in range(N):
    result += stack.pop()
  
print(result)