import sys


def main():
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    c = int(sys.stdin.readline())
    ans = 0
    ans = max(ans, (a+b)*c)
    ans = max(ans, (a*b)*c)
    ans = max(ans, (a*b)+c)
    ans = max(ans, (a+b)+c)
    ans = max(ans, a*(b*c))
    ans = max(ans, a*(b+c))
    ans = max(ans, a+(b+c))
    ans = max(ans, a+(b*c))
    print(ans)


if __name__ == "__main__":
    main()