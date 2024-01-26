class Solution:
    def addMinimum(self, word: str) -> int:
        ans = 0
        if word[0] == 'b':
            ans += 1
        elif word[0] == 'c':
            ans += 2
        
        for i, ch in enumerate(word):
            if ch == 'a':
                if i+1 < len(word):
                    if word[i+1] == 'c':
                        ans += 1
                    elif word[i+1] == 'a':
                        ans += 2
                else:
                    ans += 2
            elif ch == 'b':
                if i+1 < len(word):
                    if word[i+1] == 'a':
                        ans += 1
                    elif word[i+1] == 'b':
                        ans += 2
                else:
                    ans += 1
            elif ch == 'c':
                if i+1 < len(word):
                    if word[i+1] == 'b':
                        ans += 1
                    elif word[i+1] == 'c':
                        ans += 2
        return ans
            