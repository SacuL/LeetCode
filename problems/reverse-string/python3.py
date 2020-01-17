# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:

        len_s = len(s)
        
        if len_s == 0 or len_s == 1:
            return
        
        mid_position = len_s // 2
        
        for x in range(mid_position):
            tmp = s[x]
            s[x] = s[len_s - 1 - x]
            s[len_s - 1 - x] = tmp
            
        # or simply
        # s.reverse()
