import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        for i in range(n):
            if arr[i] == 1:
                arr[i] += 1
        
        for i in range(1, n):
            if arr[i] % arr[i-1] == 0:
                arr[i] += 1
        for num in arr:
            sys.stdout.write(f"{num} ")
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()