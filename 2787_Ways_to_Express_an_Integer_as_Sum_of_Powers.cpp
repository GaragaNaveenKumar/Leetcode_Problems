
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int MOD=1000000007;
    int k=301;
    vector<vector<int>> dp;
    int dfs(int n,int num,int x){
        if(n==0){
            return 1;
        }
        if(n<0) return 0;
        int curPower=pow(num,x);
        if(curPower>n) return 0;
        if(dp[n][num]!=-1){
            return dp[n][num];
        }
        int take=dfs(n-curPower,num+1,x);
        int skip=dfs(n,num+1,x);
        return dp[n][num]=(take+skip)%MOD;
        
        
    }
    int numberOfWays(int n, int x) {
        dp.resize(n+1,vector<int>(n+1,-1));
        return dfs(n,1,x);
        

        // vector<int> p;
        // for(int i=1;;i++){
        //     long long v=1;
        //     for(int j=0;j<x;j++) v*=i;
        //     if(v>n)break;
        //     p.push_back(v);
        // }
        // vector<long long> dp(n+1);
        // dp[0]=1;

        // for(auto& v:p){
        //     for(int s=n;s>=v;s--){
        //         dp[s]=(dp[s]+dp[s-v])%MOD;
        //     }
        // }
        // return dp[n];
        
        
    }
};