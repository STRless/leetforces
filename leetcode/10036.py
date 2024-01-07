class Solution:
    n = 8
    distances = [[[float('inf') for _ in range(2)] for _ in range(9)] for _ in range(9)]
    pq = []

    def resetDistances(self):
        for i in range(self.n+1):
            for j in range(self.n+1):
                self.distances[i][j][0] = float('inf')
                self.distances[i][j][1] = float('inf')

    def movePiece(self, moves, x, y, start, end, skip_x, skip_y, is_rook):
        v1 = [0, 0, -1, 1, 1, 1, -1, -1]
        v2 = [-1, 1, 0, 0, 1, -1, 1, -1]
        for i in range(start, end):
            nx, ny = x + v1[i], y + v2[i]
            new_moves = moves
            while 1 <= nx <= self.n and 1 <= ny <= self.n:
                if nx == skip_x and ny == skip_y:
                    if new_moves + 1 < self.distances[nx][ny][is_rook]:
                        self.distances[nx][ny][is_rook] = new_moves + 1
                        heapq.heappush(self.pq, (new_moves + 1, nx, ny))
                    new_moves += 1
                else:
                    if new_moves + 1 < self.distances[nx][ny][is_rook]:
                        self.distances[nx][ny][is_rook] = new_moves + 1
                        heapq.heappush(self.pq, (new_moves + 1, nx, ny))
                nx += v1[i]
                ny += v2[i]

    def findMinMoves(self, is_rook, skip_x, skip_y):
        while self.pq:
            moves, x, y = heapq.heappop(self.pq)
            if is_rook:
                self.movePiece(moves, x, y, 0, 4, skip_x, skip_y, is_rook)
            else:
                self.movePiece(moves, x, y, 4, 8, skip_x, skip_y, is_rook)

    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        self.resetDistances()

        heapq.heappush(self.pq, (0, a, b))
        self.distances[a][b][1] = 0
        self.findMinMoves(True, c, d)

        heapq.heappush(self.pq, (0, c, d))
        self.distances[c][d][0] = 0
        self.findMinMoves(False, a, b)
        return min(self.distances[e][f][0], self.distances[e][f][1])