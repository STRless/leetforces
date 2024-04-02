import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        arr1 = list(map(int, sys.stdin.readline().split()))
        arr2 = list(map(int, sys.stdin.readline().split()))

        if arr1 == arr2:
            sys.stdout.write("YES\n")
        else:
            flag = False
            for i in range(n):
                if arr1[i] > arr2[i]:
                    flag = True
                    break
            if flag:
                sys.stdout.write("NO\n")
            else:
                diff = -1
                i = 0
                impossible = False
                while i < n:
                    if arr1[i] == arr2[i]:
                        i += 1
                    else:
                        if diff == -1:
                            diff = arr2[i] - arr1[i]
                            j = i+1
                            while j < n:
                                if arr1[j] + diff != arr2[j]:
                                    break
                                j += 1
                            i = j
                        else:
                            impossible = True
                            break
                if impossible:
                    sys.stdout.write("NO\n")
                else:
                    sys.stdout.write("YES\n")
                    

if __name__ == "__main__":
    main()