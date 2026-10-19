class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i in nums:
            dict1[i]=i

        for i in nums:
            if target-i in dict1:
                return[nums.index(i), nums.index(target-i)]
            
        