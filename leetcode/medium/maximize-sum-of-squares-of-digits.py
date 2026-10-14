class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        
        if sum>num*9:
            return ""
        a = []

        for i in range(num):
            d=min (9,sum)
            a.append(str(d))
            sum-=d
        return "".join(a)        