class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n=len(s)
        count = [0]*26

        for ch in s:
            count[ord(ch)-ord('a')] += 1

        odd = 0 
        middle = ""

        for c in range(0,26):
            if count[c] % 2 ==1:
                odd+=1
                middle = chr(c+ord('a'))
        if odd > 1:
            return ""


        half_count = [0]*26

        for i in range(26):
            half_count[i] = count[i]//2

        half_len = n//2
        left = []

        def dfs(pos,relation):
            if pos == half_len:

                left_string = ''.join(left)

                palindrome=(left_string+middle+left_string[::-1])

                if palindrome>target:
                    return palindrome

                return None

            for i in range(26):

                if half_count[i]==0:
                    continue

                ch = chr(i+ord('a'))

                new_relation = relation

                if relation == 0:
                    if ch < target[pos]:
                        continue
                    elif ch > target[pos]:
                        new_relation = 1


                half_count[i]-=1
                left.append(ch)

                result = dfs(pos+1,new_relation)

                if result is not None:
                    return result

                left.pop()
                half_count[i]+=1    
            return None
        result = dfs(0,0)

        if result is None:
            return ""        
        return result



        