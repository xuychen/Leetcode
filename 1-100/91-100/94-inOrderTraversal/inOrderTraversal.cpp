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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> nums;
        inorderTraversalHelper(root, nums);
        return nums;
    }

    void inorderTraversalHelper(TreeNode *node, vector<int> &nums) {
        if (node) {
            inorderTraversalHelper(node->left, nums);
            nums.push_back(node->val);
            inorderTraversalHelper(node->right, nums);
        }
    }
};