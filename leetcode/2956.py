class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0, 0]
        check1, check2 = set(nums1), set(nums2)
        for num1 in nums1:
            if num1 in check2:
                ans[0] += 1
        for num2 in nums2:
            if num2 in check1:
                ans[1] += 1
        return ans