import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        big = -1
        small = -1
        if n % 2 ==1 or n < 4:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(f"{-(-n//6)} {n//4}\n")
        


if __name__ == "__main__":
    main()