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

 
        
        output=[]
        output_dict=[]
        found=False

        for i in range(0,len(str_dict)):
            for j in range(0,len(output_dict)):
                
                if str_dict[i] == output_dict[j][0]:
                    output[j].append(strs[i])
                    output_dict[j].append([str_dict[i]])
                    found = True #set flag if found
                    
                    break
            if not found:
                output.append([strs[i]])
                output_dict.append([str_dict[i]])
                
            found = False #reset flag
            




        return output