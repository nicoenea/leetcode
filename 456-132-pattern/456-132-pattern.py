class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # Stack
        if len(nums) < 3:
            return False
        stack = []
        min_array = [-1] * len(nums)
        min_array[0] = nums[0]
        for i in range(1, len(nums)):
            min_array[i] = min(min_array[i - 1], nums[i])

        for j in range(len(nums) - 1, -1, -1):
            if nums[j] <= min_array[j]:
                continue
            while stack and stack[-1] <= min_array[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])
        return False
        
        
        # Brute force time limit exceeded 
        
        # for i in range(len(nums) - 2):
        #     for j in range(i + 1, len(nums) - 1):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] < nums[k] < nums[j]:
        #                 return True
        # return False