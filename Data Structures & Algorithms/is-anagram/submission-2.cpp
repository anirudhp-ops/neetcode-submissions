class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> s_map; 
        unordered_map<char, int> t_map;
        for ( int i = 0; i < s.length(); i++) {
            if (s_map.find(s[i]) == s_map.end()) {
                s_map[s[i]] = 1; 
            }
            else {
                s_map[s[i]]++; 
            }
        }
        for ( int i = 0; i < t.length(); i++) {
            if (t_map.find(t[i]) == t_map.end()) {
                t_map[t[i]] = 1; 
            }
            else {
                t_map[t[i]]++; 
            }
        }
        if (s_map.size() != t_map.size()) 
            return false; 
        for (auto& pair : s_map) {
            if (t_map[pair.first] != pair.second) {
                return false; 
            }
        }
        return true; 
    }
};
