import sys


def main():
    password = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())

    flag = False
    start = set()
    finish = set()
    for _ in range(n):
        temp = sys.stdin.readline().strip()
        if temp == password:
            flag = True
        start.add(temp[1])
        finish.add(temp[0])
    
    if password[0] in start and password[1] in finish or flag:
        sys.stdout.write("YES")
    else:
        sys.stdout.write("NO")


if __name__ == "__main__":
    main()
