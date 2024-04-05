class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()
        count=0
        i=len(players)-1
        j=len(trainers)-1
        while i>=0 and j>=0:
            if players[i]<=trainers[j]:
                count+=1
                i-=1
                j-=1
            else:
                i-=1
        return count            
