class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        zero1, zero2 = nums1.count(0), nums2.count(0)
        if zero1 == 0:
            if zero2 + sum2 > sum1:
                return -1
            if zero2 == 0 and sum2 != sum1:
                return -1
            return sum1
        elif zero2 == 0:
            if zero1 + sum1 > sum2:
                return -1
            if zero1 == 0 and sum1 != sum2:
                return -1
            return sum2
        return max(sum1+zero1, sum2+zero2)
        