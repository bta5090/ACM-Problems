    
def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()
	
        for i in range(0, len(nums)):
            
            if len(nums) == 1:
                return False
            elif nums[i] == nums[i-1]:
                return True
        
        return False
