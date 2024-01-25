class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = [0 for _ in range(n)]
        
        checkA, checkB = set(), set()
        for i in range(n):
            checkA.add(A[i])
            checkB.add(B[i])
            temp = checkA.intersection(checkB)
            ans[i] = len(temp)
        return ans
            