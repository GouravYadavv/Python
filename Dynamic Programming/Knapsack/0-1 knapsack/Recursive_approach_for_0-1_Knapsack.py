# In this function W is the weight capacity of our sack, wt is the weight of the items and val is the value of the items respectively, while n is the number of items.
class Solution:
    def KnapSack(self, W, wt, val, n):
        def Solve(N, W):
            if W == 0 or N == 0:
                return 0
            else:
                cw = wt[N - 1]
                cval = val[N - 1]
                if cw > W:
                    return Solve(N - 1, W)
                else:
                    c1 = cval + Solve(N - 1, W - cw)
                    c2 = Solve(N - 1, W)
                    return max(c1, c2)

        return Solve(n, W)


# This program will display RunTime Error- Time Limit Exceeded because it is solved with the help of recursive function so it should be solved with the help of dynamic programming for most optimal solution.

a = Solution()
print(a.KnapSack(4, [4, 5, 1], [1, 2, 3], 3))
