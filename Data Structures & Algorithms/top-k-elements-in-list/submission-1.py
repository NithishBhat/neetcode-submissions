class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict={}

        output=[]
        bucket=[]
        for i in range(len(nums)+1):
            bucket.append([])
    
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                nums_dict[nums[i]]= nums_dict[nums[i]]+1
            else:
                 nums_dict[nums[i]]=1
        
   
        for key,value in nums_dict.items():
            bucket[value].append(key)
        

        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                output.append(j)  
                if len(output)>=k:
                    return(output)
            
     
        
        return output