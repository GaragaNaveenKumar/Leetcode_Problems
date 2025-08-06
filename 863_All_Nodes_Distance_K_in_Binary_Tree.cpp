#include<bits/stdc++.h>
using namespace std;

//  Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    unordered_map<int,int> mp;
    void dfs(TreeNode* node,unordered_map<TreeNode*,TreeNode*>& mp,unordered_map<int,int>& s,int range){
        if(s.find(node->val)!=s.end()){
            return;
        }
        s[node->val]=range;
        if(node->left!=nullptr){
            dfs(node->left,mp,s,range+1);
        }
        if(node->right!=nullptr){
            dfs(node->right,mp,s,range+1);
        }
        if(mp.count(node)){

            dfs(mp[node],mp,s,range+1);
        }
        
    }
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        vector<int> ans;
        queue<TreeNode*> q;
        unordered_map<TreeNode*,TreeNode*> mp;
        q.push(root);
        while(!q.empty()){
            TreeNode* temp=q.front();
            q.pop();
            if(temp->left!=nullptr){
                mp[temp->left]=temp;
                q.push(temp->left);
            }
            if(temp->right!=nullptr){
                mp[temp->right]=temp;
                q.push(temp->right);
            }
        }
        unordered_map<int,int> s;
        dfs(target,mp,s,0);
        for(auto& [val,range]:s){
            if(range==k){
                ans.push_back(val);
            }
        }
        return ans;
        
        
    }
};