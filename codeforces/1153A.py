import sys, math

def main():
    n, t = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    close = float('inf')
    ans = 0
    i = 1
    for a, b in arr:
        total = 0
        if a > t:
            total = a
        else:
            reach = t - a
            rem = math.ceil(reach/b)
            total = (rem * b) + a
        if total - t < close:
            close = total - t
            ans = i
        i += 1
    sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()