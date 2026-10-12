class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n= len (nums1)
        diffs=[]
        k= k1+k2
        
        for i in range(n):
            diffs.append(abs(nums1[i]-nums2[i]))
        if sum(diffs) <= k:
            return 0
        left =0
        right =max(diffs)
        while left<right:
            mid = (left + right )//2

            opr = sum(max(d-mid,0) for d in diffs)

            if opr <= k:
                right = mid
            else:
                left = mid+1
        target = left
        opr = sum(max(d-target,0) for d in diffs)
        rem = k- opr
        final = sum(min(d ,target)**2 for d in diffs)
        final -= rem * (2*target-1)
        return final






