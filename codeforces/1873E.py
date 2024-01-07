import sys
    
def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, x = map(int, sys.stdin.readline().split())
    
        heights = list(map(int, sys.stdin.readline().split()))
    
        lo, hi = 0, 999_999_999_999
    
        def condition(mid):
            water_needed = 0
            for height in heights:
                if height < mid:
                    water_needed += mid - height
            return water_needed <= x
    
        while lo < hi:
            mid = (lo + hi) // 2
    
            if not condition(mid):
                hi = mid
            else:
                lo = mid + 1
        
        sys.stdout.write("{}\n".format(lo-1))
    
    
if __name__ == "__main__":
    main()