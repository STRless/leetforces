class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ans = float('inf')
        max_score = 0
        for i, div in enumerate(divisors):
            cnt = 0
            for num in nums:
                if num % div == 0:
                    cnt += 1
            if cnt > max_score:
                max_score = cnt
                ans = div
            elif cnt == max_score:
                ans = min(ans, div)
        return ans