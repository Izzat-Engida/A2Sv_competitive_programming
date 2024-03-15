class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        min_length = min(len(s) for s in strs)
        prefix = ""
        for i in range(min_length):
            char = strs[0][i]  
            for s in strs[1:]:
                if s[i] != char:
                    return prefix  
            prefix += char

        return prefix
