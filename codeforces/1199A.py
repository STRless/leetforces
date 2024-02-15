import sys


def main():
    n, x, y = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    for i in range(n):
        flag = True

        j = i
        while j >= max(0, i-x):
            if arr[j] < arr[i]:
                flag = False
                break
            j -= 1
        
        j = i
        while j < min(n, i+y+1):
            if arr[j] < arr[i]:
                flag = False
                break
            j += 1

        if flag:
            sys.stdout.write(f"{i+1}\n")
            break
        


if __name__ == "__main__":
    main()