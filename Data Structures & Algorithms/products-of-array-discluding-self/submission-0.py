class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        product=0
        curr_index=-1
        for i in range(0,len(nums)):
            curr_index=curr_index+1
            output.append(1)
            for j in range(0,len(nums)):
                if i!=j:
                    output[curr_index]=output[curr_index]*nums[j]

        return output
            

                    