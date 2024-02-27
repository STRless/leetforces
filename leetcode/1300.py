class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        lo, hi = 0, target

        def condition(mid):
            total = 0
            for a in arr:
                total += min(mid, a)
            return abs(target - total)

        while lo < hi:
            mid = (lo + hi) // 2
            if (condition(mid) <= condition(mid+1)):
                hi = mid
            else:
                lo = mid + 1

        return lo