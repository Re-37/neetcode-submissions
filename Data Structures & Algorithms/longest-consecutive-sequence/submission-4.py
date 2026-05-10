class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        sett = set(nums)
        best = 0
        for num in nums:
            seq = 1
            while num + 1 in sett:
                seq += 1
                num += 1
            best = max(best, seq)  
        return best
