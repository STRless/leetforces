class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = dia = 0
        for (l, w) in dimensions:
            if (l**2 + w**2) > dia:
                dia = (l**2 + w**2)
                ans = l*w
            elif (l**2 + w**2) == dia:
                ans = max(ans, l*w)
        return ans