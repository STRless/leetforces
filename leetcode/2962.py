# Topics: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target = max(nums)
        left = ans = cnt = 0
        for right, num in enumerate(nums):
            cnt += num == target
            while cnt >= k:
                cnt -= nums[left] == target
                left += 1
            ans += left
        return ans