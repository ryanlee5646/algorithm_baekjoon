from sys import stdin
input = stdin.readline

N = int(input())
stack = []
now = 1
flag = True # 더이상 진행이 가능한지 여부체크

result = []

for _ in range(N): # N의 숫자 만큼 실행
  target = int(input()) # 수열의 목표 숫자
  
  if not flag:
    break
  
  if now <= N+1:
    if not stack: # 스택에 아무것도 없으면 일단 숫자 추가
      stack.append(now)
      result.append("+")
      now += 1
    
    while stack: # 숫자를 다 사용 할때까지 실행
      
      if stack[-1] == target: # 스택 맨끝 숫자가 목표 숫자랑 같으면 다음턴으로 실행
        stack.pop()
        result.append("-")
        break
      
      elif stack[-1] < target: # 스택 맨끝에 숫자가 목표 숫자보다 작을 경우 
        stack.append(now)
        result.append("+")
        now += 1
        
      elif stack[-1] > target: # 스택 맨끝에 숫자가 목표 숫자보다 클 경우
        flag = False
        break
  
if flag:
  for i in result:
    print(i)
else:
  print("NO")