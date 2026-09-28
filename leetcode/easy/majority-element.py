class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        num = nums[0]
        count = 0

        for i in nums:
            if count == 0:
                num = i
                count = 1
            else:    
                if i == num:
                    count +=1
                elif i != num:
                    count -=1                                                         
        return num                    