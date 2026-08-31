class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1
        while l<h:
            mid = (h+l)//2
            if nums[mid]>nums[h]:
                l = mid+1
            else: h = mid
        return nums[l]