import sys


def main():
    n = int(sys.stdin.readline())
    s = list(sys.stdin.readline().strip())
    t = list(sys.stdin.readline().strip())

    ans = []
    for i in range(n):
        if s[i] != t[i]:
            idx = -1
            for j in range(i+1, n):
                if s[j] == t[i]:
                    idx = j
                    break
            if idx == -1:
                sys.stdout.write("-1\n")
                return
            for j in range(idx-1, i-1, -1):
                s[j], s[j+1] = s[j+1], s[j]
                ans.append(j)
    sys.stdout.write(f"{len(ans)}\n")
    for a in ans:
        sys.stdout.write(f"{a+1} ")



if __name__ == "__main__":
    main()
