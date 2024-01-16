class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""
        for i in range(n):
            cur = ""
            cnt = 0
            for j in range(i, n):
                cur += s[j]
                if s[j] == '1':
                    cnt += 1                     
                if cnt == k:
                    if ans == "":
                        ans = cur
                    elif len(ans) > len(cur):
                        ans = cur
                    elif len(ans) == len(cur) and cur < ans:
                        ans = cur
                    break
        return ans
                
                
                