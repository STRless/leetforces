class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users = defaultdict(list)
        for i in range(len(username)):
            users[username[i]].append((website[i], timestamp[i]))
        for key, val in users.items():
            val.sort(key=lambda x: x[1])
        count = defaultdict(set)
        for key, val in users.items():
            for i in range(len(val)):
                cur = [val[i][0]]
                for j in range(i+1, len(val)):
                    cur.append(val[j][0])
                    for k in range(j+1, len(val)):
                        cur.append(val[k][0])
                        count[tuple(cur)].add(key)
                        cur.pop()
                    cur.pop()
        score = 0
        ans = []
        for key, val in count.items():
            if len(val) > score:
                score = len(val)
                ans = list(key)
            elif len(val) == score and list(key) < ans:
                ans = list(key)
        return ans
