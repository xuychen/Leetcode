#include <vector>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

using namespace std;

class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return sortedArrayToBSTHelper(nums, 0, nums.size());
    }

    TreeNode* sortedArrayToBSTHelper(vector<int> &nums, int begin, int end) {
        if (begin == end)
            return NULL;
            
        int middle = (begin + end) / 2;
        TreeNode *root = new TreeNode(nums[middle]);
        root->left = sortedArrayToBSTHelper(nums, begin, middle);
        root->right = sortedArrayToBSTHelper(nums, middle+1, end);
        return root;
    }
};