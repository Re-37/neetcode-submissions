class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        best = 1

        for num in nums:
            lenn = 1
            if num - 1 not in nums:
                while num + 1 in nums:
                    lenn += 1
                    num += 1
            best = max(lenn, best)
        return best
