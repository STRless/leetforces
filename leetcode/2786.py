class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        @cache
        def dfs(i=1, prev=-1):
            if i == len(nums):
                return 0
            
            temp = float('-inf')
            parity = 0
            if nums[i] % 2:
                parity = 1
            if prev == -1 or parity == prev:
                temp = max(temp, dfs(i+1, parity)+nums[i])
            else:
                temp = max(temp, dfs(i+1, parity)+nums[i]-x)
            temp = max(temp, dfs(i+1, prev))
            return temp
        
        return dfs(1, 1 if nums[0] % 2 else 0) + nums[0]