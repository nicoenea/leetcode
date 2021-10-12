class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        tempEven = []
        tempOdd = []
        for num in range(len(nums)):
            if nums[num] %2 == 0:
                tempEven.append(nums[num])
            else:
                tempOdd.append(nums[num])
        tempEven.extend(tempOdd)
        nums[:] = tempEven
        print(nums)
        return nums