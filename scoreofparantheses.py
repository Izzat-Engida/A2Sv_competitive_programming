class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        array=[]
        count=0
        for i in s:
            if i=='(':
                array.append(count)
                count=0
            else:
                count=array.pop()+ (1 if count==0 else 2*count)
        return count                 
        
