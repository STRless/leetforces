import sys
import math

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        m = 0
        ans = 0
        for i in range(1, n):
            if math.gcd(n, i) + i > m:
                m = math.gcd(n, i)
                ans = i
        sys.stdout.write(f"{ans}\n")


if __name__ == '__main__':
    main()