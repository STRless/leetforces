class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        suffix = nums.copy()
        suffix[-1] = nums[-1]
        for i in range(n-1, 0, -1):
            if suffix[i] >= suffix[i-1]:
                suffix[i-1] += suffix[i]
        return max(suffix)