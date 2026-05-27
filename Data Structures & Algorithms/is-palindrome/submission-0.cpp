using namespace std; 
class Solution {
public:
    bool isPalindrome(string s) {
        string valid = ""; 
        for ( int i = 0; i < s.length(); i++) {
            if (isalnum(s[i])) {
                valid += tolower(s[i]); 
            }
        }
        char* start = &valid[0]; 
        char* end = &valid[valid.length() - 1]; 
        while ( start <= end)  {
            if (*start != *end) {
                return false; 
            }
            start++; 
            end--; 
        }
        return true; 

        
    }
};
