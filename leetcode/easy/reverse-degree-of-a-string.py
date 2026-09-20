class Solution:
    def reverseDegree(self, s: str) -> int:
        answer = 0

        for i in range(len(s)):
            reverse_value = 26 - (ord(s[i]) - ord('a'))
            position = i + 1

            answer += reverse_value * position

        return answer