import sys


def main():
    n = int(sys.stdin.readline())
    arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)] 
    arr.sort()
    for i in range(n-1):
        if arr[i][0] < arr[i+1][0] and arr[i][1] > arr[i+1][1]:
            sys.stdout.write("Happy Alex")
            return
    sys.stdout.write("Poor Alex")


if __name__ == "__main__":
    main()