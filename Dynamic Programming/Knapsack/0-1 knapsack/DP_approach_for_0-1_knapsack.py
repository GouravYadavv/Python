class Solution:
    def knapsack(self, W, Wt, Val, N):
        dp = {}

        def Solve(n, W):
            if n == 0 or W == 0:
                return 0
            elif (n, W) in dp:
                return dp[(n, W)]
            else:
                cw = Wt[n - 1]
                cval = Val[n - 1]
                if cw <= W:
                    c1 = cval + Solve(n - 1, W - cw)
                    c2 = Solve(n - 1, W)
                    c = max(c1, c2)
                else:
                    c = Solve(n - 1, W)
                dp[(n, W)] = c
                return c

        return Solve(N, W)


a = Solution()
print(a.knapsack(4, [4, 5, 1], [1, 2, 3], 3))
