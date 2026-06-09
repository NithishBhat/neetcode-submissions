class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lptr=0
        rptr=len(nums)-1

        
        def subSearch(lptr,rptr):

            mid=lptr+int((rptr-lptr)/2)
            
            if nums[mid]==target:
                return mid
            elif lptr>=rptr:
                return -1
            elif target<nums[mid]:
                return subSearch(lptr,mid-1)
            elif target>nums[mid]:
                return subSearch(mid+1,rptr)
            return -1


        return subSearch(lptr,rptr)