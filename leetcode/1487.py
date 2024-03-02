class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        seen = set()
        ans = []
        for name in names:
            if name not in seen:
                seen.add(name)
                ans.append(name)
            else:
                i = 1
                while True:
                    cur = name + "(" + str(i) + ")"
                    if cur not in seen:
                        seen.add(cur)
                        ans.append(cur)
                        break
                    i += 1
        return ans