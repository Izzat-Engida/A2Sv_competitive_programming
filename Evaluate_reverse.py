class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        array=[]
        for t in tokens:
            if t in ('+-*/'):
                x=array.pop()
                y=array.pop()
                if t=='+':
                    temp=x+y
                elif t=='-':
                    temp=y-x    
                elif t=='/':
                    temp=y/x
                    temp=int(temp)    
                elif t=='*':
                    temp=y*x
                array.append(temp)
            else:
                array.append(int(t))
        return array[0]                    
