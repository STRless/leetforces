class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        check = Counter()
        winner = persons[0]
        check[winner] += 1
        self.arr = [(times[0], winner)]
        for i in range(1, len(persons)):
            p = persons[i]
            t = times[i]
            check[p] += 1
            if check[p] >= check[winner]:
                winner = p
            self.arr.append((t, winner))

    def q(self, t: int) -> int:
        idx = bisect_left(self.arr, (t, float('-inf')))
        if idx >= len(self.arr) or self.arr[idx][0] != t:
            return self.arr[max(0, idx-1)][1]
        return self.arr[idx][1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)