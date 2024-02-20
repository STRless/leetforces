import sys
     
     
def main():
    n = int(sys.stdin.readline())
    sushi = list(map(int, sys.stdin.readline().split()))

    cnt = [0, 0, 0]
    cnt[sushi[0]] += 1
    i = 1
    ans = 0
    while i < n:
        j = i
        cur = sushi[i]
        while j < n and sushi[j] == cur:
            cnt[cur] += 1
            if cur == 1:
                ans = max(ans, min(cnt[1], cnt[2]) * 2)
            elif cur == 2:
                ans = max(ans, min(cnt[1], cnt[2]) * 2)
            j += 1
        if cur == 1:
            cnt[2] = 0
        else:
            cnt[1] = 0
        i = j
    sys.stdout.write(f"{ans}\n")

    
if __name__ == "__main__":
    main()