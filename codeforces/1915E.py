import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        juices = list(map(int, sys.stdin.readline().split()))
        check = set()
        check.add('0')
        cur = 0
        flag = False
        for i, juice in enumerate(juices):
            if i % 2: juice *= -1
            cur += juice
            key = str(cur)
            if key in check:
                flag = True
                break
            check.add(key)
        if flag:
            sys.stdout.write("Yes\n")
        else:
            sys.stdout.write("No\n")


if __name__ == "__main__":
    main()