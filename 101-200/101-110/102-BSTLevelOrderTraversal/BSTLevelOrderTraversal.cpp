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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (!root)
            return result;

        queue<TreeNode *> prev_level, next_level;
        prev_level.push(root);

        while (!prev_level.empty()) {
            vector<int> int_level;
            while (!prev_level.empty()) {
                TreeNode *node = prev_level.front();
                prev_level.pop();

                if (node){
                    int_level.push_back(node->val);
                    next_level.push(node->left);
                    next_level.push(node->right);
                }
            }

            result.push_back(int_level);
            next_level.swap(prev_level);
        }

        result.pop_back();
        return result;
    }
};