#include <cmath>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        int depth = 0;
        return helper(root, depth);
    }

    bool helper(TreeNode* node, int& depth) {
        if (!node) {
            depth = 0;
            return true;
        }

        int leftDepth, rightDepth;
        bool result = helper(node->left, leftDepth) && helper(node->right, rightDepth);
        depth = max(leftDepth, rightDepth) + 1;
        return result && abs(leftDepth - rightDepth) <= 1;
    }
};