# Category: Array, Set
# Time Complexity: O(n) where n is length of nums
# Space Complexity: O(n)
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        check = set(nums)
        total_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                break
            total_sum += nums[i]
        while total_sum in check:
            total_sum += 1
        return total_sum