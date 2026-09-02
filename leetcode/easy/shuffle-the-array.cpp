class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> ans;
        ans.reserve(nums.size());
        for (int i = 0; i < n; i++) {
            ans.push_back(nums[i]);
            ans.push_back(nums[i + n]);
        }

        return ans;
    }
};
