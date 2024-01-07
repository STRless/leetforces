import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        temp = sys.stdin.readline().strip()
        if temp[0] == 'a' or temp[1] == 'b' or temp[2] == 'c':
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()