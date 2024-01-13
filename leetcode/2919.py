class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:

        @cache
        def dfs(idx=0):
            if idx > len(nums)-3:
                return 0
            
            t1 = max(0, k-nums[idx]) + dfs(idx+1)
            t2 = max(0, k-nums[idx+1]) + dfs(idx+2)
            t3 = max(0, k-nums[idx+2]) + dfs(idx+2)
            return min(t1, t2, t3)
 
        return dfs()
                    