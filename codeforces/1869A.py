import sys 


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))

        if n % 2:
            sys.stdout.write(f"4\n1 {n-1}\n1 {n-1}\n{n-1} {n}\n{n-1} {n}\n")
        else:
            sys.stdout.write(f"2\n1 {n}\n1 {n}\n")


if __name__ == "__main__":
    main()