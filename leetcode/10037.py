class Solution:

    def greedyAddToSet(self, nums, check, s, n):
        cnt = 0
        for num in nums:
            if cnt == n//2:
                break
            if num not in check:
                check.add(num)
                s.add(num)
                cnt += 1
        return cnt
    
    def addRemainingToSet(self, nums, s, cnt, n):
        for num in nums:
            if cnt == n//2:
                break
            if num not in s:
                s.add(num)
                cnt += 1

    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        check1 = set(nums1)
        check2 = set(nums2)
        s = set()
        cnt1 = self.greedyAddToSet(nums1, check2, s, n)
        cnt2 = self.greedyAddToSet(nums2, check1, s, n)
        self.addRemainingToSet(nums1, s, cnt1, n)
        self.addRemainingToSet(nums2, s, cnt2, n)
        return len(s)