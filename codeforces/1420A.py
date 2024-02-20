import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        flag = False
        for i, a in enumerate(arr):
            if i == 0:
                continue
            if a >= arr[i-1]:
                flag = True
                break
        if not flag:
            sys.stdout.write("NO\n")
        else:
            sys.stdout.write("YES\n")


if __name__ == "__main__":
    main()