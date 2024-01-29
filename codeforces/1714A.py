import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, h, m = map(int, sys.stdin.readline().split())
        best_time = 999999
        for _ in range(n):
            ah, am = map(int, sys.stdin.readline().split())
            cur_h, cur_m = h, m
            cnt = 0
            while not (cur_h == ah and cur_m == am):
                cnt += 1
                cur_m += 1
                if cur_m == 60:
                    cur_m = 0
                    cur_h += 1
                    if cur_h == 24:
                        cur_h = 0
            best_time = min(best_time, cnt)
        sys.stdout.write(f"{best_time//60} {best_time%60}\n")



if __name__ == "__main__":
    main()