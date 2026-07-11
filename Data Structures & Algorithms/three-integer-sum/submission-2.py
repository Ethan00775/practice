class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n):
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    if [nums[i],nums[j],nums[k]] not in result:
                        result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif nums[j] +nums[k] < -nums[i]: 
                    j+=1
                else: 
                    k-=1
        return result