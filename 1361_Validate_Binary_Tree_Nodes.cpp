#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool dfs(int node,vector<bool>& vis,vector<int>& l,vector<int>& r){
        if(node==-1) return true;
        if(vis[node]) return false;
        vis[node]=true;
        bool left=dfs(l[node],vis,l,r);
        bool right=dfs(r[node],vis,l,r);
        return left&right;
        
    }
    bool validateBinaryTreeNodes(int n, vector<int>& leftChild, vector<int>& rightChild) {
        vector<int> parent(n,0);
        for(int i=0;i<n;i++){
            if(leftChild[i]!=-1){
                if(i==leftChild[i]) return false;
                parent[leftChild[i]]++;
            }
            if(rightChild[i]!=-1){
                if(i==rightChild[i])return false;
                parent[rightChild[i]]++;
            }
        }
        bool oneRoot=false;
        int root;
        for(int i=0;i<n;i++){
            if(parent[i]==0){
                if(oneRoot) return false;
                else{
                    oneRoot=true;
                    root=i;
                }
            }
        }
        vector<bool> vis(n,false);

        if(dfs(root,vis,leftChild,rightChild)){
            for(auto f:vis){
                if(!f)return false;
            }
            return true;
        }else{
            return false;
        }
        

        
    }
};