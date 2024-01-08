# Category: Bit Manipulation
# Time Complexity: O(n) where n is length of nums
# Space Complexity: O(1)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        or_mask = nums[0]
        for i in range(1, len(nums)):
            or_mask ^= nums[i]
        
        ans = 0
        for i in range(32):
            if or_mask & 1 != k & 1:
                ans += 1
            or_mask >>= 1
            k >>= 1
        return ans