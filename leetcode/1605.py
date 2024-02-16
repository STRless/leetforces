class Solution:
    def restoreMatrix(self, row: List[int], col: List[int]) -> List[List[int]]:
       # 5 0 0
       # 3 4 0 
       # 0 2 8
        i = j = 0
        ans = [[0 for _ in range(len(col))] for _ in range(len(row))]
        while i < len(row) and j < len(col):
            ans[i][j] = min(row[i], col[j])
            if row[i] == col[j]:
               ans[i][j] = row[i]
               i += 1
               j += 1
            elif row[i] < col[j]:
                col[j] -= row[i]
                i += 1
            elif row[i] > col[j]:
                row[i] -= col[j]
                j += 1
        return ans