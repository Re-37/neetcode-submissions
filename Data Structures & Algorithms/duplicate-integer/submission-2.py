class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        li = []
        for num in nums:
            if num in li:
                return True
            li.append(num)
        return False
         