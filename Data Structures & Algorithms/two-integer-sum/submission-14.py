class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        tar = 0
        for i in range(len(nums)):
            tar = target - nums[i]

            if tar in seen:
                return [seen[tar], i]
            
            seen[nums[i]] = i

            