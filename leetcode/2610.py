# Topics: Array, Counting
# Time Complexity: O(n) where n is length of nums
# Space Complexity: O(n)
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        max_row = 0
        for key, val in cnt.items():
            max_row = max(max_row, val)
        ans = [[] for _ in range(max_row)]
        for key, val in cnt.items():
            for i in range(val):
                ans[i].append(key)
        return ans