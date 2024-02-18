class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        check = defaultdict(int)
        for w in wall:
            cur = 0
            for i in w:
                cur += i
                check[cur] += 1

        ans = len(wall)
        total = sum(wall[0])
        for key, val in check.items():
            if key == 0 or key == total:
                continue
            ans = min(ans, len(wall) - val)
        return ans
