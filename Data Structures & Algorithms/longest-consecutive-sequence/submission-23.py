class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums = set(nums)

        max_seq = 1
        seq = 1

        for num in nums:
            if num - 1 not in nums:

                current = num
                seq = 1

                while current + 1 in nums:
                    current += 1
                    seq += 1
                
            max_seq = max(max_seq, seq)


        return max_seq