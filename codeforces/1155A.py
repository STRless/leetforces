import sys
import math 


def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    check = list(s)

    flag = False
    for i in range(1, n):
        cur = check[i]
        prev = check[i-1]
        if cur < prev:
            flag = True
            sys.stdout.write(f"YES\n")
            sys.stdout.write(f"{i} {i+1}\n")
            return
    sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()