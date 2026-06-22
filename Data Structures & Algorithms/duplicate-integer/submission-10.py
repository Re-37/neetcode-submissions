class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett = set()

        for n in nums:
            if n not in sett:
                sett.add(n)
            else:
                return True

        return False

