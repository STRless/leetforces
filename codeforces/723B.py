import sys


def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    inside = False
    long = 0
    cnt = 0
    temp = 0

    for i in range(n):
        if s[i].isalpha():
            temp += 1
        elif s[i] == '_':
            if inside:
                if temp:
                    temp = 0
                    cnt += 1
            else:
                long = max(long, temp)
                temp = 0
        elif s[i] == '(':
            if temp:
                long = max(long, temp)
                temp = 0
            inside = True
        elif s[i] == ')':
            if temp:
                cnt += 1
                temp = 0
            inside = False
    long = max(long, temp)
    sys.stdout.write(f"{long} {cnt}\n")



if __name__ == "__main__":
    main()