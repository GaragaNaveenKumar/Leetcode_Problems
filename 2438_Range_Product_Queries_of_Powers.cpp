#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    
    vector<int> productQueries(int n, vector<vector<int>>& queries) {
        vector<int> powers;
        long long MOD=1000000007;
        for(int i=0;i<32;i++){
            if((n&(1<<i))!=0){
                powers.push_back(1<<i);
            }
        }
        vector<int> ans(queries.size());
        for(int i=0;i<queries.size();i++){
            long long product=1;
            for(int j=queries[i][0];j<=queries[i][1];j++){
                product=(1ll*product*powers[j])%MOD;
                // product%=MOD;
            }
            ans[i]=product;
        }
        return ans;
        
        
        
    }
};