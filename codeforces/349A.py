import sys


def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    r25, r50 = 0, 0
    flag = True
    for a in arr:
        if a == 25:
            r25 += 1
        elif a == 50:
            if r25 >= 1:
                r25 -= 1
            else:
                flag = False
            r50 += 1
        else:
            if r25 >= 1 and r50 >= 1:
                r25 -= 1
                r50 -= 1
            elif r25 >= 3:
                r25 -= 3
            else:
                flag = False
    if flag:
        sys.stdout.write("YES")
    else:
        sys.stdout.write("NO")


if __name__ == "__main__":
    main()