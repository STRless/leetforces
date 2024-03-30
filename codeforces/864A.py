import sys
from collections import Counter


def main():
    n = int(sys.stdin.readline())
    arr = Counter([int(sys.stdin.readline()) for _ in range(n)])
    flag = True
    if len(arr) == 2:
        temp = float('inf')
        flag = True
        c = []
        for key, val in arr.items():
            if temp == float('inf'):
                temp = val
            else:
                if temp != val:
                    flag = False
            c.append(key)
        if flag:
            sys.stdout.write("YES\n")
            sys.stdout.write(f"{c[0]} {c[1]}\n")
        else:
            print("NO")
    else:
        print("NO")


if __name__ == "__main__":
    main()