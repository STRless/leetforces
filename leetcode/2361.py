# Topics: DP
# Time Complexity: O(n)
# Space Compleixty: O(n)
class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        n = len(regular)
        ans = [0 for _ in range(n)]

        @cache
        def dfs(i=n-1, exp=False):
            if i < 0:
                return 0
            
            temp = float('inf')

            if exp:
                temp = min(temp, dfs(i-1, False) + regular[i])
                temp = min(temp, dfs(i-1, exp) + express[i])
            else:
                temp = min(temp, dfs(i-1, exp) + regular[i])
                temp = min(temp, dfs(i-1, True) + expressCost + express[i])

            return temp
            
        for i in range(n):
            ans[i] = dfs(i)
        
        return ans

