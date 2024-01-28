class Solution:
    def coloredCells(self, n: int) -> int:
        ans = 1
        mul = 0
        for i in range(1, n+1):
            ans += (4*mul)
            mul+=1
        return ans
            