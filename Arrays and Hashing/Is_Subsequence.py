class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        point_s = point_t = 0   # implementing two pointer approach

        while ( point_s < len(s) and point_t < len(t) ):   # loop through all letters in t
            if ( s[point_s] == t[point_t] ):   # if letters are equal to each other
                point_s += 1   # increment pointer in string s
            point_t += 1   # always increment pointer in string t
        
        return point_s == len( s )   # return is the pointer to s is the same as the length of string s