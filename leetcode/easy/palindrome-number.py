class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False        

        rev = 0

        while x > rev:
            r = x % 10 
            rev = rev * 10 + r
            x = x // 10
        return x == rev or x == rev // 10        