import sys


def main():
    board = [sys.stdin.readline().strip() for _ in range(4)]

    v1 = [0, 0, -1, 1, 1, 1, -1, -1]
    v2 = [-1, 1, 0, 0, -1, 1, -1, 1]
    for i in range(4):
        for j in range(4):
            if board[i][j] == 'x':
                for k in range(8):
                    x, y = i, j
                    cnt = 0
                    space = 0
                    while x < 4 and y < 4 and x >= 0 and y >= 0:
                        if board[x][y] == 'x':
                            cnt += 1
                        elif board[x][y] == '.':
                            space += 1
                        else:
                            break
                        if cnt == 3 or (cnt == 2 and space == 1):
                            print("YES")
                            return
                        x += v1[k]
                        y += v2[k]

    print("NO")



if __name__ == "__main__":
    main()