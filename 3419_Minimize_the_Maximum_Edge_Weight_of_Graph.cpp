#include<bits/stdc++.h>
using namespace std;



class Solution {
public:
    int minMaxWeight(int n, vector<vector<int>>& edges, int threshold) {
        sort(edges.begin(),edges.end(),[](vector<int> &a,vector<int> &b){
            return a[2]<b[2];
        });
        int low=edges[0][2],high=edges.back()[2],ans=-1;

        //using binary search to get minimum weight required to graph.
        while(low<=high){
            int mid=(low+high)/2;
            if(check(n,edges,mid)){
                ans=mid;
                high=mid-1;
            }else{
                low=mid+1;
            }
        }
        return ans;
        
    }

    //function to check can we create entire graph by using weight limit.
    bool check(int n,vector<vector<int>>& edges,int maxw){
        vector<vector<int>> graph(n);
        for(const auto& edge:edges){
            if(edge[2]>maxw)break;
            graph[edge[1]].push_back(edge[0]);
        }

        vector<int> vis(n,0);
        dfs(0,vis,graph);
        for(auto& v:vis){
            if(v==0)return false;
        }
        return true;
    }

    //dfs function to traverse connected graph.
    void dfs(int node,vector<int>& vis,vector<vector<int>>& graph){
        vis[node]=1;
        for(auto& neibor:graph[node]){
            if(!vis[neibor]){
                dfs(neibor,vis,graph);
            }
        }
    }
};