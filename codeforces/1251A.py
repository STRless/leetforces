import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        s = sys.stdin.readline().strip()
        i = 0
        n = len(s)
        check = set()
        while i < n:
            j = i
            cnt = 0
            while j < n and s[j] == s[i]:
                if cnt >= 2:
                    break
                if s[j] == s[i]:
                    cnt += 1
                j += 1
            if cnt == 1:
                check.add(s[i])
            i = j
        
        ans = list(check)
        ans.sort()
        print("".join(ans))




if __name__ == "__main__":
    main()