class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_count={}
        for i in nums:
            if i in num_count:
                return True
            else:
                num_count[i]=1
        return False   