# 스택

'''
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
'''

from sys import stdin
input = stdin.readline

arr = []

N = int(input())

for i in range(N):
    a = list(input().split())
    if a[0] == 'push':
        arr.append(a[1])
    elif a[0] == 'pop':
        if not len(arr):
            print(-1)
        else:
            print(arr.pop())
    elif a[0] == 'size':
        print(len(arr))
    elif a[0] == 'empty':
        if len(arr):
            print(0)
        else:
            print(1)
    else:
        if len(arr):
            print(arr[-1])
        else:
            print(-1)


