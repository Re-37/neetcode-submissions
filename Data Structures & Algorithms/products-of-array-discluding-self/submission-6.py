class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        listt = []

        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt +=  1
        
        if zero_cnt > 1: 
            return [0] * len(nums)
        
        for i in range(len(nums)):
            if zero_cnt:
                if nums[i] == 0:
                    listt.append(prod)
                else:
                    listt.append(0)
            else:
                listt.append(prod // nums[i])
        
        return listt
        