class Solution:
    def minInsertions(self, s: str) -> int:
        need = 0
        answer = 0

        for i in s:
            if i == '(':
                need += 2        
                if need % 2 ==1:
                    need -=1
                    answer+=1


            else:
                need-=1
                if need < 0:
                    need = 1
                    answer+=1
        return answer + need        
