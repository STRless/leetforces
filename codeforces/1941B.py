import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        flag = False
        for i in range(n-2):
            if arr[i] < 0:
                flag = True
                break
            temp = arr[i]
            arr[i] -= temp
            arr[i+2] -= temp
            arr[i+1] -= 2*temp
        if flag or arr[-1] != 0 or arr[-2] != 0:
            print("NO")
        else:
            print("YES")


if __name__ == "__main__":
    main()