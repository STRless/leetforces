class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9+7
        i = 0
        j = len(nums) - 1
        ans = 0
        while i <= j:
            if nums[i] + nums[j] <= target:
                ans += pow(2, j-i, mod)
                ans %= mod
                i += 1
            else:
                j -= 1
        return ans
