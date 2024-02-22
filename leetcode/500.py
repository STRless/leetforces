class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        check = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

        ans = []
        for word in words:
            idx = 0
            if word[0].lower() in check[1]:
                idx = 1
            elif word[0].lower() in check[2]:
                idx = 2
            
            flag = True
            for ch in word[1:]:
                if ch.lower() not in check[idx]:
                    flag = False
                    break
            if flag:
                ans.append(word)
        return ans
