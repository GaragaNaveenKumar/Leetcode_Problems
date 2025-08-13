#include <bits/stdc++.h>
using namespace std;

class DSU{
    public:
        vector<int> parent;
        DSU(){
            for(int i=0;i<=1000;i++){
                parent.push_back(i);
            }
            
        }
        int find(int x){
            if(parent[x]!=x){
                parent[x]=find(parent[x]);
            }
            return parent[x];
        }
        bool un(int x,int y){
            int xr=find(x),yr=find(y);
            if(xr==yr){
                return false;
            }
            parent[yr]=xr;
            return true;
        }
};
class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        vector<pair<int,pair<int,int>>> g;
        for(int i=0;i<points.size();i++){
            int x=points[i][0],y=points[i][1];
            for(int j=i+1;j<points.size();j++){
                int x1=points[j][0],y1=points[j][1];
                int dist=abs(x-x1)+abs(y-y1);
                g.push_back({dist,{i,j}});

            }
        }
        sort(g.begin(),g.end(),[](auto a,auto b){
            return a.first<b.first;
        });
        int ans=0;
        DSU d;
        for(int i=0;i<g.size();i++){
            auto a=g[i];
            auto b=a.second;
            if(d.un(b.first,b.second)){
                ans+=a.first;
            }
        }

        return ans;

        
    }
};