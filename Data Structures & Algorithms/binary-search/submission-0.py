class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = (int)(len(nums)//2)
        if(nums[mid]==target):
            return mid
        elif(len(nums)<=1):
            return -1
        elif(target<nums[mid]):
            return self.search(nums[0:mid],target)
        else:
            res = self.search(nums[mid:],target)
            return res + mid if res != -1 else -1