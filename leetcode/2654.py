class Solution:
    def minOperations(self, nums: List[int]) -> int:
        change = 0
        ones = nums.count(1)
        n = len(nums)
        if ones > 0:
            return n - ones
        
        min_ops = float('inf')
        for i in range(n-1):
            cur = nums[i]
            for j in range(i+1, n):
                cur = gcd(cur, nums[j])
                if cur == 1:
                    min_ops = min(min_ops, j-i)
        if min_ops == float('inf'):
            return -1
        return min_ops-1 + n