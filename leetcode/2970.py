class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                temp = []
                flag = True
                for k in range(len(nums)):
                    if k < i or k > j:
                        if temp and temp[-1] >= nums[k]:
                            flag = False
                        else:
                            temp.append(nums[k])
                if flag:
                    ans += 1
        return ans