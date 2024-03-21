class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        answer=""
        i=0
        while i<len(command):
            if command[i]=='G':
                answer+=command[i]
                i+=1
            elif command[i]=='(' and command[i+1]=='a':
                answer+="al"
                i+=4
            else:
                answer+='o'  
                i+=2     
        return answer        
