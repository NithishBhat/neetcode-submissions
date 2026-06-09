class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lptr=0
        rptr=len(nums)-1
        output=-1
        
        def subSearch(lptr,rptr):
            nonlocal output
            mid=lptr+int((rptr-lptr)/2)
            
            if nums[mid]==target:
                output= mid
            elif lptr>=rptr:
                return -1
            elif target<nums[mid]:
                subSearch(lptr,mid-1)
            elif target>nums[mid]:
                subSearch(mid+1,rptr)
            return output


        return subSearch(lptr,rptr)