# Topics: Sorting, Counting
# Time Complexity: O(n*nlogn)
# Space Complextiy: O(n)
class Solution:
    def maximumLength(self, s: str) -> int:
        check = defaultdict(list)
        ans = -1
        cur = ""
        cnt = 0
        for ch in s:
            if cur == "":
                cnt = 1
                cur = ch
            elif cur != ch:
                check[cur].append(cnt)
                cnt = 1
                cur = ch
            else:
                cnt += 1
        check[cur].append(cnt)
        for key, val in check.items():
            val.sort()
            for i, v in enumerate(val):
                if v > 2:
                    ans = max(ans, v-2)
                if i+1 < len(val) and val[i+1] > v:
                    ans = max(ans, v)
                if i+1 < len(val) and val[i+1] == v:
                    if v > 1:
                        ans = max(ans, v-1)
                if i+2 < len(val):
                    ans = max(ans, v)
        return ans