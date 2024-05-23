class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> counts ;

        for( auto& num : nums ) {
            if ( counts[num] >= 1 ) {
                return true ;
            } else {
                counts[num]++ ;
            }
        }

        return false ;
    }
};