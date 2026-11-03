class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        output=[0]*len(temperatures)
        
        for i in range(0,len(temperatures)):
            if stack!=[]:
            
                while stack!=[] and temperatures[i] > stack[-1][0]:
                   
                    temp=stack.pop()
                    output[temp[1]]=i-temp[1]
                
                stack.append((temperatures[i],i))
            else:
                stack.append((temperatures[i],i))



        return output
   
