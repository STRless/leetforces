import sys

# Topics: Greedy
# Time Complexity: O(nm)
# Space Complexity: O(1) not including input


def main():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n, m, tile1, tile2 = map(int, sys.stdin.readline().split())
        grid = [sys.stdin.readline().strip() for _ in range(n)]

        flag = False 
        if tile1 * 2 < tile2:
            flag = True 
        
        ans = 0
        for i in range(n):
            j = 0
            while j < m:
                if flag:
                    if grid[i][j] == '.':
                        ans += tile1
                else:
                    if j+1 < m and grid[i][j] == '.' and grid[i][j+1] == '.':
                        ans += tile2
                        j += 1
                    elif grid[i][j] == '.':
                        ans += tile1
                j += 1

        sys.stdout.write("{}\n".format(ans))


if __name__ == "__main__":
    main()