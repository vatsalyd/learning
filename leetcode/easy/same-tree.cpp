/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == nullptr && q == nullptr) return true; // Both nodes are null
        if (p == nullptr || q == nullptr) return false; // One node is null and the other is not

        // Check if current nodes have the same value and recursively check left and right subtrees
        return p->val == q->val && 
               isSameTree(p->left, q->left) && 
               isSameTree(p->right, q->right);
    }
};

// Helper function to create a tree for testing
TreeNode* buildTree(const std::vector<int>& nodes, int i = 0) {
    if (i >= nodes.size() || nodes[i] == -1) return nullptr;
    TreeNode* root = new TreeNode(nodes[i]);
    root->left = buildTree(nodes, 2 * i + 1);
    root->right = buildTree(nodes, 2 * i + 2);
    return root;
}
