from sys import stdin
input = stdin.readline


def change_direction(direction):
    if direction == 0 or direction == 2:
        direction += 1
    elif direction == 1 or direction == 3:
        direction -= 1
    return direction


def move(horse_num):
    y, x, d = chess_horse[horse_num]
    nx = x + dx[d]
    ny = y + dy[d]

    # 파란색 칸이거나 맵을 벗어난 경우
    if 0 > nx or nx >= n or 0 > ny or ny >= n or chess_map[ny][nx] == 2:
        d = change_direction(d)
        # 방향을 반대로 바꿔줌
        chess_horse[horse_num][2] = d
        nx = x + dx[d]
        ny = y + dy[d]
        # 반대방향으로 이동했는데 또 파란색이거나 맵을 벗어 났으면 제자리
        if 0 > nx or nx >= n or 0 > ny or ny >= n or chess_map[ny][nx] == 2:
            return True

    horse_tmp = []
    for i, j in enumerate(horse_map[y][x]):
        if j == horse_num:
            horse_tmp.extend(horse_map[y][x][i:])
            horse_map[y][x] = horse_map[y][x][:i]
            break

    if chess_map[ny][nx] == 1:
        horse_tmp = horse_tmp[-1::-1]

    for h in horse_tmp:
        chess_horse[h][0], chess_horse[h][1] = ny, nx
        horse_map[ny][nx].append(h)

    if len(horse_map[ny][nx]) >= 4:
        return False
    return True


n, k = map(int, input().split())
chess_map = [list(map(int, input().split())) for _ in range(n)]
horse_map = [[[] for _ in range(n)] for _ in range(n)]
dx = [1, -1, 0, 0]  # 동 서 북 남
dy = [0, 0, -1, 1]

chess_horse = []

for i in range(k):
    y, x, d = map(int, input().split())
    # 체스말 정보를 말 순서대로 배열에 추가
    chess_horse.append([y-1, x-1, d-1])  # 좌표, 방향 1씩 빼줘야함
    # 좌표에 말 추가
    horse_map[y-1][x-1].append(i)

# 턴 횟수
turn = 0

while True:
    flag = False

    if turn > 1000:
        print(-1)
        break
    for i in range(k):
        if move(i) == False:
            flag = True
            break
    turn += 1
    if flag:
        print(turn)
        break