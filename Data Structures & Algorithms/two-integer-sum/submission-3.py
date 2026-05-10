class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        table = {}
        res = 0
        for i in range(len(nums)):
            res = target - nums[i]
            if res in table:
                return [table.get(res), i]
            table[nums[i]] =  i


        