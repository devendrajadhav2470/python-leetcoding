class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low = 0
        high = n-1

        while low<=high:
            mid = (low+high) // 2

            # low = 0 , high = 4 , mid = 2
            if target == nums[mid] or nums[low]==target or nums[high]==target:
                return True
            if nums[low]>nums[high]:
                # low is in the first part, high is in the second part
                if nums[mid]==target:
                    return True
                if nums[mid]>=nums[low]:
                    # mid lies in the first part 
                    if nums[mid] > target:
                        # target will lie to the left of mid or in the second part (to the right) 
                        if target==nums[high]:
                            return True
                        if target>nums[high]:
                            # target in first part left of mid 
                            high = mid - 1
                        elif target<nums[high]:
                            # target lies in the second part 
                            low = mid + 1
                    else:
                        # target bigger than mid , mid in first part -> target lies to the right of mid 
                        low = mid + 1

                else:
                    # mid is in the second part
                    if nums[mid] > target:
                        # target lies to the left 
                        high = mid-1
                    else:
                        # target lies to the right of mid ??
                        # or it can also lie in the first part ?
                        if target>nums[low]:
                            # target lies in the first part 
                            high = mid - 1 
                        elif target==nums[low]:
                            return True
                        else:
                            # target lies in the second part
                            low = mid + 1
            elif nums[low]==nums[high]:
                # high can be on the second part or it can also be on the first part
                # if high in the first part then low to high all will be equal, then we already know target not exist
                # best case is if high in the second part  
                if nums[mid] > nums[high]:
                    # this means that mid lies in the first part 
                    if target > nums[mid]:
                        low = mid + 1 
                    else:
                        low = low + 1
                        high = high - 1

                    
                elif nums[mid] < nums[high]:
                    # this means that mid lies in the second part 
                    if target < nums[mid]:
                        high = mid - 1
                    else:
                        low = low + 1
                        high = high - 1
                else:
                    # this means mid is equal to high as well -> all three  equal  [ ...low....mid..high...] or
                    # [...low..mid....high]
                    # the target can lie between low to mid or between mid to high 
                    # we already know it isn't between mid to high  
                    low = low + 1
                    high = high - 1

                    # # case 1 mid lies in the second part 
                    # if nums[]
                    #     if target > nums[mid]:
                    #         high = mid - 1
                    #     else:
                    #         high = mid - 1
                    
                    # # case 2 mid lies in the first part 
                    # if target > nums[mid]:
                    #     low = mid + 1
                    # else: 
                    #     low = mid + 1

                        # target is less thatn low
                        
                    # if target > nums[mid]:
                    #     low = mid + 1 
                    # else:
                    #     high = mid -1 

                    
            else:
                # high is also in the first part to the right of low 
                if nums[mid] == target:
                    return True
                if nums[mid] > target:
                    high = mid -1 
                else:
                    low = mid + 1
            


        return False