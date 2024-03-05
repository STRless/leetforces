import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        if 360 % (180 - n) == 0:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")
            

if __name__ == "__main__":
    main()