#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> powerOf2;
    void findPowerOf2(){
        for(int i=0;i<32;i++){
            powerOf2.push_back(1<<i);
        }
    }
    unordered_map<char,int> findFreq(int n){
        string k=to_string(n);
        unordered_map<char,int> mp;
        for(auto& ch:k){
            mp[ch]++;
        }
        return mp;

    }
    bool check(unordered_map<char,int>& freq,int pow){
        unordered_map<char,int> freqPow=findFreq(pow);

        for(auto& [ch,cnt]:freq){
            if(cnt!=freqPow[ch]){
                return false;
            }
        }
        for(auto& [ch,cnt]:freqPow){
            if(!freq.count(ch)){
                return false;
            }
        }
        return true;

    }
    bool reorderedPowerOf2(int n) {
        if(!powerOf2.size()){
            findPowerOf2();
        }
        unordered_map<char,int> freqOfN=findFreq(n);
        for(auto& pow:powerOf2){
            if(check(freqOfN,pow)){
                return true;
            }
        }
        return false;

        
    }
};