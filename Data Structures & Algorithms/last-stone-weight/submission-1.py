class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def popMaxWeight():
            print(stones)
            maxWeight=max(stones)
            stones.pop(stones.index(max(stones)))
            return maxWeight

        while stones:
            max_1=popMaxWeight()
            max_2=popMaxWeight()
            if max_1 != max_2:
                newWeight=max_1-max_2
                stones.append(newWeight)

            if len(stones)==1:
                return stones[0]
        
        return 0
            



        

