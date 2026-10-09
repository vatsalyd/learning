class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        st =strs[0]
        for i in range(len(st)):
            ch = st[i]
            for word in strs[1:]:
                if i >= len(word) or word[i] != ch:
                    return st[:i]
        return st            