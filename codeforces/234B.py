import sys


def main():
    f = open("input.txt", "r")
    n, k = map(int, f.readline().split())
    arr = list(map(int, f.readline().split()))
    check = []
    for i, a in enumerate(arr):
        check.append((i+1, a))
    
    check.sort(key=lambda x: -x[1])
    mi = float('inf')
    ans = []
    for i in range(k):
        mi = min(mi, check[i][1])
        ans.append(check[i][0])
    
    b = open("output.txt", "w")
    sys.stdout = b
    print(mi)
    for i in ans:
        print(f"{i}", end = " ")
    b.close()
    f.close()


if __name__ == "__main__":
    main()