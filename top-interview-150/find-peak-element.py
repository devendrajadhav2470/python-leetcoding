from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # runs in O(log n) time
        n = len(nums)
        neg_inf = - pow(2,31) -1
        left = 0 
        right = n-1
        prev_left = None
        prev_right = None
        while left<=right and (left!=prev_left or prev_right != right):
            prev_left = left
            prev_right = right
            mid = (left+right+1) // 2
            left_val = nums[mid-1] if mid>=1 else neg_inf
            right_val = nums[mid+1] if mid<n-1 else neg_inf
            if nums[mid] > left_val and nums[mid] > right_val:
                return mid
            elif nums[mid] > left_val and nums[mid] < right_val:
                left = mid+1
            elif nums[mid] < left_val and nums[mid] > right_val:
                right = mid-1
            else:
                right = mid-1
            