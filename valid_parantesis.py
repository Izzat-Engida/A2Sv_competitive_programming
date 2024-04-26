class Solution:
    def isValid(self, s: str) -> bool:
        temp=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                temp.append(s[i])
            elif s[i] == ')' or s[i] == ']' or s[i] == '}':
                if not temp:
                    return False
                t=temp[-1]
                if (s[i]=='}' and t!='{') or  (s[i]==']' and t!='[') or (s[i]==')' and t!='('):
                    return False
                else:
                    temp.pop()
        return not temp                     

        
