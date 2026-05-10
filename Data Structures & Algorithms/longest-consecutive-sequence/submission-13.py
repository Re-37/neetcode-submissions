class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        nums = sorted(nums)
        print(nums)
        best = 1
        temp = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i] + 1 == nums[i+1]:
                temp += 1 
            else:
                temp = 1
            best = max(temp, best)
        return best
