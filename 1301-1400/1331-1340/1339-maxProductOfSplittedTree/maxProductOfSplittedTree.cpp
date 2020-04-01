#include <vector>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int maxProduct(TreeNode* root) {
        vector<int> sums;
        int totalSum = sumOfNodes(root, sums);
        long maxProduct = 0;

        for (auto it: sums) {
            long product = (long) it(totalSum - it);
            if (product > maxProduct)
                maxProduct = product;
        }

        return maxProduct % ((int) 1e9 + 7);
    }

    int sumOfNodes(TreeNode *node, vector<int> &sums) {
        if (!node)
            return 0;

        sums.push_back(node->val + sumOfNodes(node->left, sums) + sumOfNodes(node->right, sums));
        return sums.back();
    }
};