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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> nums;
        preorderTraversalHelper(root, nums);
        return nums;
    }

    void preorderTraversalHelper(TreeNode* node, vector<int> &nums) {
        if (!node)
            return;

        nums.push_back(node->val);
        preorderTraversalHelper(node->left, nums);
        preorderTraversalHelper(node->right, nums);
    }
};