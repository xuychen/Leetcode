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
    int kthLargest(TreeNode* root, int k) {
        int count = 0;
        return helper(root, k, count)->val;
    }

    TreeNode* helper(TreeNode* node, int k, int& count) {
        if (!node) {
            count = 0;
            return NULL;
        }

        int left_count, right_count;
        TreeNode* right = helper(node->right, k, right_count);
        TreeNode* left = NULL;

        count = ++right_count;
        if (right_count < k)
            left = helper(node->left, k-right_count, left_count);
        else if (right_count == k)
            return node;
        else
            return right;

        count += left_count;
        return left;
    }
};