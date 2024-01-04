class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = sum(nums)
        for i in reversed(range(len(nums))):
            if nums[i] < ans - nums[i]:
                break
            ans -= nums[i]

        return -1 if ans == 0 else ans