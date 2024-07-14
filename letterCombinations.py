class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        comb={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        n=len(digits)
        ans=[]
        if digits=="":
            return []
        def backtrack(temp,i):
            if len(temp)==n:
                ans.append(temp)
                return
            if i>=n:
                return
            word=comb[digits[i]]
            for char in word:
                backtrack(temp+char,i+1)    

        backtrack("",0)     
        return ans         



        
