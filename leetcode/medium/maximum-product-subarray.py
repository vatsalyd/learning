class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_n=nums[0] 
        min_n=nums[0]
        ans=nums[0]

        for i in nums[1:]:
            if i < 0:
                max_n ,min_n=min_n,max_n

            max_n = max(i*max_n,i)
            min_n= min(i*min_n ,i)
            ans=max(ans,max_n)
        return ans    

