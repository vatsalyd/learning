class Solution:
    def reverse(self, x: int) -> int:

        sign = 1

        if x < 0:
            sign = -1
            x = -x

        limit = 2**31 - 1 if sign == 1 else 2**31

        reverse = 0

        while x > 0:

            digit = x % 10

            if reverse > limit // 10:
                return 0

            if reverse == limit // 10 and digit > limit % 10:
                return 0

            reverse = reverse * 10 + digit

            x //= 10

        return sign * reverse
        