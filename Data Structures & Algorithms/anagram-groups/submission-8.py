class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        str_dict=[]

        for word in strs:
            temp={}
            for j in word:
                if j in temp:
                    temp[j]=temp[j]+1
                else:
                    temp[j]=1

            str_dict.append(temp)

 
        
        output={}

        for i in range(0,len(str_dict)):
            x=tuple(sorted(str_dict[i].items()))
      
            if x in output:
                output[x].append(strs[i])
            else:
                output[x]=[strs[i]]

            


        

        return list(output.values())