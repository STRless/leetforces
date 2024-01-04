import sys
from collections import defaultdict
import heapq


def solve(n, m, adj, slow):
    distance = [[float('inf') for _ in range(1001)] for _ in range(n)]
    distance[0][slow[0]] = 0
    pq = []
    heapq.heappush(pq, (0, slow[0], 0)) # dist, bike, cur

    while pq:
        cur_dis, cur_bike, cur_city = heapq.heappop(pq)

        for nei, wei in adj[cur_city]:
            new_dis = cur_dis + (wei * cur_bike)
            if new_dis < distance[nei][cur_bike]:
                distance[nei][cur_bike] = new_dis
                heapq.heappush(pq, (new_dis, min(cur_bike, slow[nei]), nei))

    return min(distance[n-1])


def main():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        adj = defaultdict(list)
        for _ in range(m):
            u, v, w = map(int, sys.stdin.readline().split())
            adj[u-1].append((v-1, w))
            adj[v-1].append((u-1, w))
        slowness = list(map(int, sys.stdin.readline().split()))
        sys.stdout.write("{}\n".format(solve(n, m, adj, slowness)))


if __name__ == "__main__":
    main()