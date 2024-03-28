import sys


def main():
    n = int(sys.stdin.readline())
    temp = list(map(int, sys.stdin.readline().split()))
    prog = temp[0] - temp[1]
    flag = True
    for i in range(n-1):
        if temp[i] - temp[i+1] != prog:
            flag = False
            break
    if flag:
        print(temp[-1] - prog)
    else:
        print(temp[-1])


if __name__ == "__main__":
    main()