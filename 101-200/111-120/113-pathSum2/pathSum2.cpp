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
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<int> path;
        vector<vector<int>> result;
        pathSumHelper(root, sum, path, result);
        return result;
    }

    void pathSumHelper(TreeNode* node, int sum, vector<int> &path, vector<vector<int>> &result) {
        if (!node)
            return;

        path.push_back(node->val);
        if (!node->left && !node->right && sum == node->val)
            result.push_back(path);
        else {
            pathSumHelper(node->left, sum-node->val, path, result);
            pathSumHelper(node->right, sum-node->val, path, result);
        }

        path.pop_back();
    }
};