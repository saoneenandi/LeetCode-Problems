class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(board)

        dp = [[(-1, 0) for _ in range(n)] for _ in range(n)]
        dp[-1][-1] = (0, 1)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or (i == n - 1 and j == n - 1):
                    continue

                best, ways = -1, 0
                for x, y in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                    if x < n and y < n:
                        s, w = dp[x][y]
                        if s > best:
                            best, ways = s, w
                        elif s == best:
                            ways = (ways + w) % MOD

                if ways:
                    dp[i][j] = (
                        best + (0 if board[i][j] in 'ES' else int(board[i][j])),
                        ways
                    )

        return list(dp[0][0]) if dp[0][0][1] else [0, 0]