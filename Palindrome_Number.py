class Solution(object):
    def isPalindrome(self, x):
        temp=x
        if(temp<0):
            return False
        else:
           j=0 
           while(x!=0):
               j=j*10+x%10
               x=x/10   
        x=j 
        return temp==x;  
        
