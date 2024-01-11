class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                idx = (j + k) + 1
                if idx > len(mat[i]):
                    idx = idx % len(mat[i])
                if mat[i][j] != mat[i][idx-1]:
                    return False
        return True