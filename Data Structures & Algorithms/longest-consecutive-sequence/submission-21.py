class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums = sorted(set(nums))

        max_seq = 1
        seq = 1

        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                seq += 1
                max_seq = max(max_seq, seq)
            else:
                seq = 1

        return max_seq