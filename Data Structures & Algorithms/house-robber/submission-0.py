class Solution:
    def rob(self, nums: List[int]) -> int:
        len_nums=len(nums)
        rob_max=0

        for i in range(len_nums):
            temp=0
            for j in range(i,len_nums,2):
                temp=nums[j]+temp
                if j+2>len_nums-1:
                    break
            rob_max=max(rob_max,temp)
        return rob_max