import sys


def main():
    n = int(sys.stdin.readline())
    money = list(map(int, sys.stdin.readline().split()))
    if 1 not in money:
        print(1)
    else:
        print(-1)



if __name__ == "__main__":
    main()