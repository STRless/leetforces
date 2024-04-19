import sys

def main():
    n, k = map(int, sys.stdin.readline().split())

    arr = list(map(int, sys.stdin.readline().split()))

    changes = 0
    i = 0
    while i < n:
        if changes >= k:
            break
        if arr[i] < 0:
            arr[i] *= -1
            changes += 1
        else:
            break
        i += 1
    arr.sort()
    if changes < k and (k-changes)%2:
        arr[0] *= -1
    
    ans = sum(arr)
    sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()