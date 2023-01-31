class Solution {
public:
    void reverseString(vector<char>& s) {
    
        int y=s.size()/2;
        for(int i=0,j=s.size()-1;i<y;i++,j--)
        {
            swap(s[i],s[j]);
        }
    }
};
