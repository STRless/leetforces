import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))


        flag = False
        for i in range(n):
            pre = -1
            post = -1
            for j in range(i):
                if arr[j] < arr[i]:
                    pre = j+1
                    break
            for j in range(i+1, n):
                if arr[j] < arr[i]:
                    post = j+1
                    break
            if pre != -1 and post != -1:
                sys.stdout.write("YES\n")
                sys.stdout.write(f"{pre} {i+1} {post}\n")
                flag = True
                break

        if not flag:
            sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()