import sys


def main():
    n = int(sys.stdin.readline())
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    ones = a.count('1')
    zeros = a.count('0')
    ans = 0
    for i in range(n):
        if b[i] == '0':
            if a[i] == '1':
                ans += zeros
                ones -= 1
            else:
                ans += ones
                zeros -= 1
    sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()