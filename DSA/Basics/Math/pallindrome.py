class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        a = x
        while x > 0:
            digit = x % 10
            reverse = (reverse * 10) + digit
            x = x // 10
        if reverse == a:
            print(reverse, a)
            return True
        else:
            print(reverse, a)
            return False


a = Solution()
print(a.isPalindrome(121))
