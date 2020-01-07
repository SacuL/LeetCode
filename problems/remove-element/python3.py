# https://leetcode.com/problems/remove-element/submissions/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        final_num_position = -1
        
        if( len(nums) > 0 and nums[0] != val ):
            final_num_position = 0

        
        for i in range(1, len(nums)):
            if(nums[i] != val):
                final_num_position = final_num_position + 1
                nums[final_num_position] = nums[i]
                            
        
        return final_num_position + 1;
