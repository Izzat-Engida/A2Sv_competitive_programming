class Solution:
    def numRabbits(self, answers):
        temp = {}
        sum = 0
        for i in answers:
            if i > 0:
                if i not in temp or temp[i] == 0:
                    temp[i] = i
                    sum += i + 1
                else:
                    temp[i] -= 1
            else:
                sum += 1
        return sum
