class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [nums[0]], [nums[1]]
        s1, s2 = [nums[0]], [nums[1]]
        for num in nums[2:]:
            val = num
            idx1, idx2 = bisect.bisect_right(s1, val), bisect.bisect_right(s2, val)
            cnt1, cnt2 = len(arr1) - idx1, len(arr2) - idx2
            if cnt1 > cnt2 or (cnt1 == cnt2 and len(arr1) <= len(arr2)):
                arr1.append(val)
                s1.insert(idx1, val)
            else:
                arr2.append(val)
                s2.insert(idx2, val)
        return arr1 + arr2