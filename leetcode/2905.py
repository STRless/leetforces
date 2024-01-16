class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        min_idx, max_idx = 0, 0
        n = len(nums)
        for i in range(indexDifference, n):
            if nums[i-indexDifference] < nums[min_idx]:
                min_idx = i-indexDifference
            if nums[i-indexDifference] > nums[max_idx]:
                max_idx = i-indexDifference
            
            if abs(nums[i] - nums[min_idx]) >= valueDifference:
                return [min_idx, i]
            if abs(nums[i] - nums[max_idx]) >= valueDifference:
                return [max_idx, i]
        return [-1, -1]
            