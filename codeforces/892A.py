import sys


def main():
    n = int(sys.stdin.readline())
    a1 = list(map(int, sys.stdin.readline().split()))
    a2 = list(map(int, sys.stdin.readline().split()))
    a2.sort(reverse=True)
    if sum(a1) <= a2[0] + a2[1]:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")

        

if __name__ == "__main__":
    main()