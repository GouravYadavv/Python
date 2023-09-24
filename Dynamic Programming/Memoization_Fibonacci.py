# In this program we have converted a recursion function which is commonly used for fibonacci number of small value to the dynamic programming.

"""
The Code for recursion function would have been;

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


Here in this code out problem is divided into subproblem but is solved multiple times for same subproblem which is not considered as optimal and is one of the biggest drawback of recursion which let's see how we can overcome this problem with the use of dynamic programming.
"""


def fib(n, dp):
    if n == 0:
        return n
    elif n == 1:
        return 1
    elif dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fib(n - 1, dp) + fib(n - 2, dp)
        return dp[n]


print(fib(510, [-1] * (511)))
