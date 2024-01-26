class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = 0
        max_cnt = 0
        for i in range(m):
            cnt = mat[i].count(1)
            if cnt > max_cnt:
                max_cnt = cnt
                ans = i
        return [ans, max_cnt]
            