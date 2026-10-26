class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans(nums.size(),0);
        int pre = 1;
        for(int i=0;i<nums.size();i++){
            ans[i] = pre;
            pre *= nums[i];
        }
        int back = 1;
        for(int j=nums.size()-1;j>=0;j--){
            ans[j] *= back;
            back *= nums[j];
        }
        return ans;
    }
};
