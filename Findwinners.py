class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = {}
        for l in matches:
            if l[0] not in losers:
                losers[l[0]] = 0
            losers[l[1]] = losers.get(l[1], 0) + 1

        temp1, temp2 = [], []
        for a,b in losers.items():
            if b == 0:
                temp1.append(a)
            if b == 1:
                temp2.append(a)
        temp1.sort()
        temp2.sort()
        return [temp1, temp2]

