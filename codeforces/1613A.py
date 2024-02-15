import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        x1, p1 = map(int, sys.stdin.readline().split())
        x2, p2 = map(int, sys.stdin.readline().split())
        temp1 = str(x1) + ('0'*p1)
        temp2 = str(x2) + ('0'*p2)
        if len(temp1) < len(temp2):
            sys.stdout.write("<\n")
        elif len(temp1) > len(temp2):
            sys.stdout.write(">\n")
        else:
            if temp1 < temp2:
                sys.stdout.write("<\n")
            elif temp1 > temp2:
                sys.stdout.write(">\n")
            else:
                sys.stdout.write("=\n")


if __name__ == "__main__":
    main()