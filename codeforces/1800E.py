import sys
from collections import defaultdict


class Node:
    
    def __init__(self, p):
        self.p = p
        self.rank = 0


def find(subsets, x):
    while subsets[x].p != x:
        subsets[x].p = subsets[subsets[x].p].p
        x = subsets[x].p
    return x


def union(subsets, u, v):
    a, b = find(subsets, u), find(subsets, v)

    if subsets[a].rank > subsets[b].rank:
        subsets[b].p = a
    elif subsets[a].rank <= subsets[b].rank:
        subsets[a].p = b


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()
        t = sys.stdin.readline().strip()
    
        subsets = [Node(i) for i in range(n)]

        for i in range(n):
            if i + k < n:
                union(subsets, i, i+k)
            if i + k + 1 < n:
                union(subsets, i, i+k+1)
        
        flag = True
        check = [[0 for _ in range(26)] for _ in range(n)]
        for i in range(n):
            root = find(subsets, i)
            ind1 = ord(s[i]) - ord('a') 
            ind2 = ord(t[i]) - ord('a')
            check[root][ind1] += 1
            check[root][ind2] -= 1
        
        for i in range(n):
            for j in range(26):
                if check[i][j]:
                    flag = False

        ans = "YES" if flag else "NO"
        sys.stdout.write("{}\n".format(ans))


if __name__ == "__main__":
    main()