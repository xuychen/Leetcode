// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int rob(TreeNode* root) {
        int takeMax, ntakeMax;
        robHelper(root, takeMax, ntakeMax);
        return max(takeMax, ntakeMax);
    }

    void robHelper(TreeNode *node, int &takeMax, int &ntakeMax) {
        int ltakeMax, rtakeMax, lntakeMax, rntakeMax;

        if (!node) {
            takeMax = 0;
            ntakeMax = 0;
            return;
        }

        robHelper(node->left, ltakeMax, lntakeMax);
        robHelper(node->right, rtakeMax, rntakeMax);

        takeMax = node->val + lntakeMax + rntakeMax;
        ntakeMax = max(ltakeMax, lntakeMax) + max(rtakeMax, rntakeMax); 
    }
};