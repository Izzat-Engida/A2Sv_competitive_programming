class Solution:
    def smallestNumber(self, num: int) -> int:
        if  (num>=0 and num<=9) or(num<= -1 and num>= -9): 
            return num
        temp=[]
        typ=False
        if num<0:
            typ=True
            num=num*-1
        while num>0:
            temp.append(num%10)
            num=num//10
        temp=sorted(temp,reverse=typ)
        if not typ and 0 in temp:
            for i in range(1, len(temp)):
                if temp[i] != 0:
                    temp[0], temp[i] = temp[i], temp[0]
                    break
        num = 0
        for i in range(len(temp)):
            num = num * 10 + temp[i]
        return -num if typ else num
