class Solution:
    def splitString(self, s: str) -> bool:

        def backtrack(idx=0, prev=-1):
            if idx == len(s) and prev != int(s):
                return True
            cur = ""
            flag = False
            for i in range(idx, len(s)):
                cur += s[i]
                if prev == -1:
                    flag |= backtrack(i+1, int(cur))
                elif prev - int(cur) == 1:
                    flag |= backtrack(i+1, int(cur))
            return flag
        
        return backtrack()
