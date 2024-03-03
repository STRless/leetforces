import sys


def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    choice = min(arr)
    for a in arr:
        if a % choice:
            sys.stdout.write("-1\n")
            return
    
    sys.stdout.write(f"{choice}\n")


if __name__ == "__main__":
    main()