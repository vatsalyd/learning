class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr = nums[0]
        best_sum = nums[0]

        for num in nums[1:]:
            curr = max(num , curr +num)
            best_sum = max(curr,best_sum)
        return best_sum    