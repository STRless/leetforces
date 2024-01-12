import sys, math

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        if n == 2:
            sys.stdout.write("-1\n")
            continue
        start, end = 1, math.ceil((n**2)/2)+1
        arr = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if (i + j) % 2:
                    arr[i][j] = end
                    end += 1
                else:
                    arr[i][j] = start
                    start += 1
        for i in range(n):
            for j in range(n):
                sys.stdout.write(f"{arr[i][j]} ")
            sys.stdout.write(f"\n")


if __name__ == "__main__":
    main()