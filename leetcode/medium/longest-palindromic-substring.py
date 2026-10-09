class Solution:
    def longestPalindrome(self, s: str) -> str:
        end =0
        start=0

        for i in range(len(s)):
            right =i
            left =i
            while left>=0 and right <len(s) and s[left]==s[right]:
                if right-left > end -start:
                    end = right 
                    start = left
                    
                left-=1
                right+=1

            left = i
            right = i+1

            while left>=0 and right <len(s) and s[left]==s[right]:
                if right -left>end-start:
                    start = left
                    end = right

                right +=1
                left -=1
        return s[start:end+1]        

                