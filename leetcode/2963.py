# Topics: Counting, DP, Combinatorics
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        last_idx = defaultdict(int)
        for i, num in enumerate(nums):
            last_idx[num] = i

        @cache
        def dfs(cur=0):
            if cur == n:
                return 1
            
            left, right = cur, last_idx[nums[cur]]

            while left < right:
                right = max(right, last_idx[nums[left]])
                left += 1
            
            temp = 1
            if cur > 0:
                temp = 2
            return (dfs(right+1)*temp) % (10**9+7)
        
        return dfs()