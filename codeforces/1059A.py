import sys


def main():
    n, l, a = map(int, sys.stdin.readline().split())
    arr = []
    for _ in range(n):
        arr.append(tuple(map(int, sys.stdin.readline().split())))
    ans = 0
    if n > 0:
        temp = arr[0][0]
        ans += temp // a
        temp = arr[-1][0] + arr[-1][1]
        ans += (l-temp) // a
        for i in range(n):
            if i != 0:
                temp = arr[i-1][0] + arr[i-1][1]
                ans += (arr[i][0] - temp) // a
    else:
        ans += l // a
    
    print(ans)


if __name__ == "__main__":
    main()