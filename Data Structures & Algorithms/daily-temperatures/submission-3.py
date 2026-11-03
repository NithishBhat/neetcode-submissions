class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        output=[None]*len(temperatures)
        
        for i in range(0,len(temperatures)):
            if stack!=[]:
            
                while stack!=[] and temperatures[i] > stack[-1][0]:
                    print(stack)
                    print(output)
                    print((i,count))
                    print("***********")
                    temp=stack.pop()
                    output[temp[1]]=i-temp[1]
                
                stack.append((temperatures[i],i))
            else:
                stack.append((temperatures[i],i))


            for i in range(0,len(output)):
                if  output[i]==None:
                    output[i]=0

        return output
   
