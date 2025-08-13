#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s){
        int start=0,end=s.size()-1;
        while(start<=end){
            if(s[start]!=s[end]) return false;
            start++;
            end--;
        }
        return true;
    }

    void helper(int idx,string& s,vector<vector<string>>& result,vector<string>& curSplit){
        if(idx==s.size()){
            result.push_back(curSplit);
            return;
        }
        for(int i=idx;i<s.size();i++){
            string str=s.substr(idx,i-idx+1);
            if(isPalindrome(str)){
                curSplit.push_back(str);
                helper(i+1,s,result,curSplit);
                curSplit.pop_back();
            }
        }
    }
    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> curSplit;
        helper(0,s,result,curSplit);
        return result;
        
    }
};