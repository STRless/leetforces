import sys


def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    temp = []
    for i, a in enumerate(arr):
        temp.append((i+1, a))
    
    temp.sort(key=lambda x: -x[1])

    ans = 0
    cnt = 0
    for i, t in temp:
        ans += cnt * t + 1
        cnt += 1
    
    sys.stdout.write(f"{ans}\n")
    for i, t in temp:
        sys.stdout.write(f"{i} ")


if __name__ == "__main__":
    main()