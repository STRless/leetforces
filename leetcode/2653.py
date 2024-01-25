class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        cnt = defaultdict(int)
        for i in range(k-1):
            cnt[nums[i]] += 1
        
        i = 0
        for j in range(k-1, len(nums)):
            cnt[nums[j]] += 1
            if j - i >= k:
                cnt[nums[i]] -= 1
                i += 1
            
            beauty = 0
            x_cnt = x
            for k in range(-50, 0):
                if x_cnt - cnt[k] <= 0:
                    beauty = k
                    break
                x_cnt -= cnt[k]
            ans.append(beauty)

        return ans