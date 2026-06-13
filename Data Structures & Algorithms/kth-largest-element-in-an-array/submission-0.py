class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lptr=0
        rptr=1
        nums=sorted(nums)
        return nums[k+1]