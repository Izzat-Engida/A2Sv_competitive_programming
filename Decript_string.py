class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp1 = "abcdefghi"
        temp2 = "jklmnopqrstuvwxyz"
        n = len(s) - 1
        ns = ""
        temp = ""
        while n >= 0:
            if s[n] == '#':
                temp = s[n - 2] + s[n - 1]
                n -= 3
                o = int(temp)
                ns = temp2[o - 10]+  ns
            else:
                temp = s[n]
                n -= 1
                o = int(temp)
                ns =  temp1[o - 1]+ ns
        return ns
