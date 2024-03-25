import sys


def get_cost(c):
    return ord(c) - ord('a') + 1


def main():
    n, k = map(int, sys.stdin.readline().split())
    s = list(sys.stdin.readline().strip())
    s.sort()
    ans = float('inf')
    for i in range(len(s)):
        total = get_cost(s[i])
        prev = total
        cnt = 1
        for j in range(i+1, len(s)):
            if cnt == k:
                break
            cur = get_cost(s[j])
            if cur - prev >= 2:
                total += cur
                prev = cur
                cnt += 1
        if cnt == k:
            ans = min(ans, total)

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()