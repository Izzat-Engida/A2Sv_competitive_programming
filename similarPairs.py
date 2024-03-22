class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        i=0
        c=0
        while i<len(words):
            j=i+1
            while j<len(words):
                if set(words[i])==set(words[j]):
                    c+=1
                j+=1 
            i+=1
        return c    

