import sys 


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        sys.stdin.readline()

        grid = []
        for _ in range(8):
            grid.append(sys.stdin.readline().strip())
        
        visited = [[False for _ in range(8)] for _ in range(8)]
        red = True
        for i in range(8):
            for j in range(8):
                if not visited[i][j] and grid[i][j] == 'B':
                    cnt = 0
                    for k in range(8):
                        if grid[k][j] != 'B':
                            break
                        cnt += 1
                        visited[k][j] = True
                    if cnt == 8:
                        red = False
        if red:
            sys.stdout.write("R\n")
        else:
            sys.stdout.write("B\n")
                    

if __name__ == "__main__":
    main()