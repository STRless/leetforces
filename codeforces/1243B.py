import sys


def main():
    k = int(sys.stdin.readline())
    for _ in range(k):
        n = int(sys.stdin.readline())
        s = list(sys.stdin.readline().strip())
        t = list(sys.stdin.readline().strip())
        flag = False
        cnt = 0
        check = []
        for i in range(n):
            if s[i] != t[i]:
                check.append((s[i], t[i]))
                cnt += 1
        if cnt == 2 and check[0] == check[1]:
            print("Yes")
        else:
            print("No")



if __name__ == "__main__":
    main()