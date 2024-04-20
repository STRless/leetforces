import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        a1, a2, a3, a4 = map(int, sys.stdin.readline().split())
        if a1 == 0:
            sys.stdout.write("1\n")
            continue
        ans = a1 + (min(a2, a3)*2) + min(a1+1, abs(a2-a3)+a4)
        sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()