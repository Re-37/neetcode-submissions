class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        table = {}
        
        for i in range(len(nums)):
            table[nums[i]] = table.get(nums[i], 0) + 1
    
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in table.items():
            buckets[value].append(key)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result




        