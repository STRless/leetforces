import sys


def main():
    a1 = int(sys.stdin.readline())
    a2 = int(sys.stdin.readline())
    k1 = int(sys.stdin.readline())
    k2 = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    temp1 = a1 * (k1-1)
    temp2 = a2 * (k2-1)
    mi = 0
    if temp1+temp2 < n:
        mi = min(a1+a2, n - (temp1+temp2))
    
    ma = 0
    if k1 < k2:
        ma = min(a1, n//k1)
        sub = k1 * ma
        sub = n - sub
        ma += min(a2, sub//k2)
    else:
        ma = min(a2, n//k2)
        sub = k2 * ma
        sub = n - sub
        ma += min(a1, sub//k1)
    
    print(mi, ma)


if __name__ == "__main__":
    main()