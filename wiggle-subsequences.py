class Solution:
    dp = {}
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        mx = 1
        for i in range(n):
            mx = max(mx,self.helper(nums,i,None))
        return mx
    def helper(self, nums, curr, prev_num):
        # starting at curr give me the largest subseq 
        mx = 1
        for i in range(curr+1,len(nums)):
            # to take 
            if prev_num:
                if (nums[i]-nums[curr]) * (nums[curr]-nums[prev_num]) < 0:
                    mx = max(mx,1+self.helper(nums,i, curr))
                continue
            print("Hi")
            mx = max(mx,1+self.helper(nums,i, curr))
        return mx