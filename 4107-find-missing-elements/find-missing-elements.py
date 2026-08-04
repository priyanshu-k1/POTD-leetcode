class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        start = nums[0]
        end = nums[-1]
        nums = set(nums)
        output=[]
        for i in range(start,end+1):
            if i not in nums:
                output.append(i)
        return output



        