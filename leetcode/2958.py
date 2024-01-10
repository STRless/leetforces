class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i = ans = 0
        cnt = defaultdict(int)
        for j in range(len(nums)):
            cnt[nums[j]] += 1

            while cnt[nums[j]] > k:
                cnt[nums[i]] -= 1
                i += 1
            
            ans = max(ans, j - i + 1)
        return ans