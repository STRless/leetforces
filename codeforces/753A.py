import sys


def main():
    n = int(sys.stdin.readline())
    cur = 0
    cnt = 0
    for i in range(1, n+1):
        if cur + i <= n:
            cur += i
            cnt += 1
        else:
            break
    
    sys.stdout.write(f"{cnt}\n")
    cur = 0
    for i in range(1, cnt+1):
        if i == cnt:
            sys.stdout.write(f"{n-cur}\n")
        else:
            cur += i
            sys.stdout.write(f"{i} ")


if __name__ == "__main__":
    main()