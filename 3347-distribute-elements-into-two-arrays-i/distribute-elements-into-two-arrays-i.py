class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arrOne = []
        arrTwo =[]
        n = len(nums)
        arrOne.append(nums[0])
        arrTwo.append(nums[1])
        for i in range(2,n):
            if arrOne[-1] > arrTwo[-1]:
                arrOne.append(nums[i])
            else:
                arrTwo.append(nums[i])
        return arrOne+arrTwo