#include <queue>
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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> nums;
        postorderTraversalHelper(root, nums);
        return nums;
    }

    void postorderTraversalHelper(TreeNode* node, vector<int> &nums) {
        if (!node)
            return;

        postorderTraversalHelper(node->left, nums);
        postorderTraversalHelper(node->right, nums);
        nums.push_back(node->val);
    }
};