import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        total = sum(arr)
        if total % 3 == 0:
            sys.stdout.write("0\n")
        else:
            cnt = 1
            while True:
                if (cnt+total) % 3 == 0:
                    break
                cnt += 1
            flag = False
            for a in arr:
                if (total - a) % 3 == 0:
                    flag = True
            if flag:
                sys.stdout.write("1\n")
            else:
                sys.stdout.write(f"{cnt}\n")


if __name__ == "__main__":
    main()