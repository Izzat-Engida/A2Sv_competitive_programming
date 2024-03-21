class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort()
        word=words[0]
        answer=[]
        for j in word:
            check=True
            for i in range(1,len(words)):
                if j not in words[i]:
                    check=False
                    break
                else:
                    words[i]=words[i].replace(j,'',1)    
            if check: 
                answer.append(j)
        return answer               


           
