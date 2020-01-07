# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        final_num_position = 0
        
        for i in range(1, len(nums)):
            if(nums[i] != nums[final_num_position]):
                final_num_position = final_num_position + 1
                nums[final_num_position] = nums[i]
                            
        
        return final_num_position + 1;
                
            
            
            
        
