class Solution {
    public List<String> stringMatching(String[] words) {
        Arrays.sort(words,(a,b)->Integer.compare(a.length(),b.length()));
        List<String> res= new ArrayList<>();
        for(int i=0;i<words.length-1;i++){
            for(int j=words.length-1;j>i;j--){
                if(words[i].length()>words[j].length()) break;
                else{
                    if (words[j].contains(words[i])){
                        res.add(words[i]);
                        break;
                    }
                }
            }
        }
        return res;
        
    }
}