class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        flag = False
        ans = []
        temp = ""
        for s in source:
            i = 0
            while i < len(s):
                if not flag and i+1 < len(s) and s[i] == '/' and s[i+1] == '/':
                    break
                elif not flag and i+1 < len(s) and s[i] == '/' and s[i+1] == '*':
                    flag = True
                    i += 2
                elif flag and i+1 < len(s) and s[i] == '*' and s[i+1] == '/':
                    flag = False
                    i += 2
                elif not flag:
                    temp += s[i]
                    i += 1
                else:
                    i += 1
            if temp == "" or flag:
                continue
            ans.append(temp)
            if not flag:
                temp = ""
        return ans