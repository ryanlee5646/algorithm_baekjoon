N = int(input())
data = list(map(int, input().split()))
stack = []

for i in range(N):
  while(stack):

    if data[i] > data[stack[-1]]: # 오큰수를 찾았으면 스택에서 pop한 인덱스 값을 오큰수로 바꿔줌
      data[stack.pop()] = data[i]
    else: # 오큰수가 아니면 stack에 오큰수를 못찾은 수의 인덱스를 추가해줌
      stack.append(i)
      break
    
  if not stack:
    stack.append(i)

for i in stack:
  data[i] = -1

print(*data)  
  
    

