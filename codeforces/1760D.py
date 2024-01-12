import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))

        cnt = 0
        prev = -1
        i = 0
        while i < n:
            j = i+1
            flag = False
            while j < n and arr[j] == arr[i]:
                flag = True
                j += 1
            if flag:
                if i == 0 or arr[i-1] > arr[i]:
                    if j == n or arr[j] > arr[j-1]:
                        cnt += 1
            else:
                if (i == 0 or arr[i-1] > arr[i]) and (i+1 == n or arr[i+1] > arr[i]):
                    cnt += 1

            i = j
        if cnt == 1:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()