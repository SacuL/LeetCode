# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
    
        negative = x < 0

        x = abs(x)

        x_str = str(x)

        x_list = list(x_str)

        x_list.reverse()

        x_joined = "".join(x_list)

        x_int = int(x_joined)

        if(negative):
            if(x_int >= 2147483648):
                return 0
            return -x_int
        elif(x_int >= 2147483647):
            return 0
        else:
            return x_int
