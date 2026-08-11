class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        lookUp = set(nums)
        seqSum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                seqSum += nums[i]
            else:
                break
        if seqSum not in lookUp:
            return seqSum
        while(seqSum in lookUp):
            seqSum += 1
        return seqSum
        