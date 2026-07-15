class Solution:
    
    def hasDuplicate(self, nums: List[int]) -> bool:
        output = False
        numset = set(nums)

        if len(nums) != len(numset):
            output = True
        
        return output
                

