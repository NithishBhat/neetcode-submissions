class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict={}
        nums_list=[]
        output=[]
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                nums_dict[nums[i]]= nums_dict[nums[i]]+1
            else:
                 nums_dict[nums[i]]=1
        
        for key,value in nums_dict.items():
            nums_list.append([value,key])
        
        nums_list=sorted(nums_list,reverse=True)
        print(nums_list)
        for i in nums_list[:k]:
            output.append(i[1])
        
        return output