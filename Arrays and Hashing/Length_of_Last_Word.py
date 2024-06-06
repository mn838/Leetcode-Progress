class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split()   # take all leading and trailing whitespace off and split by " "

        return len( s_list[ len( s_list ) - 1 ] )   # return the length of the last word in the list