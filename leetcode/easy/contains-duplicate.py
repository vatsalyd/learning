class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for i in range(len(nums)):
            if nums[i] not in duplicate:
                duplicate[nums[i]] = i
            else:
                return True    
        return False                