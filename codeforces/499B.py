import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    mydict = {}
    for _ in range(m):
        a, b = map(str, sys.stdin.readline().split())
        mydict[a] = b
    
    arr = list(map(str, sys.stdin.readline().split()))
    for a in arr:
        if len(mydict[a]) < len(a):
            sys.stdout.write(f"{mydict[a]} ")
        else:
            sys.stdout.write(f"{a} ")


if __name__ == "__main__":
    main()