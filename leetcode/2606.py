class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        best_sum = 0
        cur_sum = 0
        for ch in s:
            cost = 0
            if ch in chars:
                cost = vals[chars.index(ch)]
            else:
                cost = (ord(ch)-ord('a')+1)
            cur_sum = max(cost, cur_sum+cost)
            best_sum = max(best_sum, cur_sum)
        return best_sum
                