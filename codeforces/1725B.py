import sys

def main():
    n, d = map(int, sys.stdin.readline().split())
    players = list(map(int, sys.stdin.readline().split()))
    players.sort(reverse=True)

    def condition(mid):
        cnt = 0
        back = n - 1
        for i, player in enumerate(players):
            total = player
            while i < back and total <= d:
                total += player
                back -= 1
            if i <= back and total > d:
                cnt += 1
        return cnt >= mid

    lo, hi = 0, n+1

    while lo < hi:
        mid = (lo + hi) // 2

        if not condition(mid):
            hi = mid
        else:
            lo = mid + 1
    
    sys.stdout.write("{}\n".format(lo-1))


if __name__ == "__main__":
    main()