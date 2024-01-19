class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        cnt = Counter(nums)
        return n+1 == len(nums) and len(cnt) == n and cnt[n] == 2