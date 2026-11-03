class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]*len(temperatures)
        output=[]
   
        if temperatures==[]:
            stack.append(temperatures[0])
        for i in range(1,len(temperatures)):
            count=1
            while stack and temperatures[i]>stack[-1]:
                print(i+"-"+count)
                output[i-count]=stack.pop()
                count=count+1
            stack.append(temperatures[i])
        return output
            