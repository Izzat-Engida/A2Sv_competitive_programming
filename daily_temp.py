class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer=[0]*len(temperatures)
        array=[]
        for temp in range(len( temperatures)):
            while array and temperatures[temp]> temperatures[array[-1]]:
                i =array.pop()
                answer[i]=temp-i
            array.append(temp)      
        return answer        


        
