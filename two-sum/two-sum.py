class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(i, num) for i, num in enumerate(nums)]
        nums = sorted(nums, key=lambda x: x[1])
        
        left, right = 0, len(nums)-1
        
        while (nums[left][1] + nums[right][1] != target):
            if nums[left][1] + nums[right][1] < target:
                left += 1
            else:
                right -= 1
        
        return [nums[left][0], nums[right][0]]