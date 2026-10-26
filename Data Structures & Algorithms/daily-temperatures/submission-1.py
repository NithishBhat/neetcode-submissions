class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        count=0
        output=[]
        found=False
        for i in range(0,len(temperatures)):
            for j in range(i,len(temperatures)):
                
                if temperatures[i]<temperatures[j]:
                    found=True
                    output.append(count)
                    count=0
                    break
                count=count+1
            if not found:
                output.append(0)
            found=False
            count=0
        return output