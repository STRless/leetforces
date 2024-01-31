import sys

def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    n *= 2
    check = arr
    check.sort()
    if sum(check[:n//2]) != sum(check[n//2:n]):
        for num in check:
            sys.stdout.write(f"{num} ")
        sys.stdout.write("\n")
    else:
        sys.stdout.write("-1")
        

if __name__ == "__main__":
    main()