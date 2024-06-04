class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_seen = {}   # initializing the hashset for string s
        t_seen = {}   # initializing the hashset for string t

        for letters in s:
            s_seen[letters] = s_seen.get(letters, 0) + 1   # add the letters to the hashset and increment the count of the letters
        
        for letters in t:
            t_seen[letters] = t_seen.get(letters, 0) + 1   # add the letters to the hashset and increment the count of the letters

        return s_seen == t_seen   # return true if the hashsets are equal else return false