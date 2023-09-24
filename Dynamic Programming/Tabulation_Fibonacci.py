# In this method we will ne creating a table first consist of all the values we want.

# Let's create a table to get a fibonacci number answer until 100th number.

dp = [0] * 101
dp[0] = 0
dp[1] = 1
for i in range(
    2, 100
):  # We are not including range from 0 as we have already given the first 2 values.
    dp[i] = dp[i - 1] + dp[i - 2]

# We are all set to go now, all we have to do is to write the number between the range of our table which will instantly give the answer of the value we want. It will take extra space in out memory as extra values which might not came into use in our program are also stored in the memory but it is one of the fastest way.
print(dp[77])
print(dp[11])
