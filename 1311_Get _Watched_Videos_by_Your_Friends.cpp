#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    queue<int> bfs(vector<vector<int>>& friends,int l,int id){
        queue<int> q;
        q.push(id);
        unordered_set<int> vis;
        vis.insert(id);
        while(l--){
            int n=q.size();
            for(int i=0;i<n;i++){
                int person=q.front();
                q.pop();
                for(auto& f:friends[person]){
                    // cout<<f<<" ";
                    if(!vis.count(f)){
                        q.push(f);
                        vis.insert(f);
                    }

                }
            }
            // cout<<endl;
        }
        return q;
    }
    vector<string> watchedVideosByFriends(vector<vector<string>>& watchedVideos, vector<vector<int>>& friends, int id, int level) {
        queue<int> q=bfs(friends,level,id);
        unordered_map<string,int> freq;
        while(q.size()){
            int person=q.front();
            q.pop();
            // cout<<person<<endl;
            for(auto& movie:watchedVideos[person]){
                // cout<<movie<<endl;
                freq[movie]++;
            }
        }
        vector<string> ans;
        for(auto& [movie,cnt]:freq){
            ans.push_back(movie);
            
        }
        sort(ans.begin(),ans.end(),[&](auto a,auto b){
            if(freq[a]<freq[b]) return true;
            if(freq[a]==freq[b]) return a<b;
            return false;
        });
        return ans;
        
    }
};