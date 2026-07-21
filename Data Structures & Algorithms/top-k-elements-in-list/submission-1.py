class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}

        List = []

        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        sortedKeys = sorted(dict, key=lambda x: dict[x], reverse=True)

        List = sortedKeys[:k]

                
        return List
