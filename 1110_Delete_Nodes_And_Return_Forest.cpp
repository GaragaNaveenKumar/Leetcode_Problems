#include<bits/stdc++.h>
using namespace std;


 // Definition for a binary tree node.
 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };
 
class Solution {
public:
    
    TreeNode* dfs(TreeNode* root,unordered_set<int>& to_delete,vector<TreeNode*>& res){
        if(root==nullptr) return nullptr;
        root->left=dfs(root->left,to_delete,res);
        root->right=dfs(root->right,to_delete,res);
        if(to_delete.count(root->val)){
            if(root->left!=nullptr)res.push_back(root->left);
            if(root->right!=nullptr)res.push_back(root->right);
            delete root;
            return nullptr;

        }else{
            return root;
        }
    }
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        vector<TreeNode*> res;
        unordered_set<int> delete_val;
        for(auto& val:to_delete){

            delete_val.insert(val);
        }
        root=dfs(root,delete_val,res);
        if(root!=nullptr) res.push_back(root);
        return res;

        
    }
};