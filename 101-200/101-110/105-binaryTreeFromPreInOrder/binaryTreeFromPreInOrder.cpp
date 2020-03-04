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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return buildTreeHelper(preorder, 0, inorder, 0, inorder.size());
    }

    TreeNode *buildTreeHelper(vector<int> &preorder, int pre_index, vector<int> &inorder, int left, int right) {
        if (left == right)
            return NULL;

        int middle_value = preorder[pre_index];
        int in_index = find(inorder, middle_value, left, right);
        TreeNode *root = new TreeNode(middle_value);
        root->left = buildTreeHelper(preorder, pre_index+1, inorder, left, in_index);
        root->right = buildTreeHelper(preorder, pre_index+in_index-left+1, inorder, in_index+1, right);
        return root;
    }

    int find(vector<int> &nums, int num, int start, int end) {
        for (int i = start; i < end; ++i)
            if (nums[i] == num)
                return i;

        return -1;
    }
};