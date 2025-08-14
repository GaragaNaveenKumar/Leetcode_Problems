#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int,int>>> g(n+1);
        for(const auto& x:times){
            g[x[0]].push_back({x[1],x[2]});
        }
        vector<int> time(n+1,INT_MAX);
        time[k]=0;
        queue<pair<int,int>> q;
        q.push({k,0});

        while(!q.empty()){
            const auto [cur,curTime]=q.front();
            q.pop();
            for(auto& [nei,t]:g[cur]){
                if(t+curTime<time[nei]){
                    time[nei]=t+curTime;
                    q.push({nei,t+curTime});
                }
            }
        }
        int maxTime=0;
        for(int i=1;i<=n;i++){
            maxTime=max(maxTime,time[i]);

        }
        if(maxTime==INT_MAX) return -1;
        else return maxTime;
        
    }
};