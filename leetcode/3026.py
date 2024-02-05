class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:        
        n = len(nums)
        ans = float('-inf')
        check = {}
        cur = 0
        for num in nums:
            check[num] = min(check.get(num, float('inf')), cur)
            cur += num

            if  num + k in check:
                ans = max(ans, cur - check[num+k])
            if num - k in check:
                ans = max(ans, cur - check[num-k])
        if ans == float('-inf'):
            return 0
        return ans
