class Solution:
    def firstOccurence(self,arr,tar,n):
        low = 0
        high = n - 1
        sol = -1
        while low <= high:
            mid = low + (high - low)//2
            if arr[mid] == tar:
                sol = mid
                high = mid - 1
            elif arr[mid] > tar:
                high = mid - 1
            else:
                low = mid + 1
        return sol
    def lastOccurence(self,arr,tar,n):
        low = 0
        high = n - 1
        sol = -1
        while low <= high:
            mid = low + (high - low)//2
            if arr[mid] == tar:
                sol = mid
                low = mid + 1
            elif arr[mid] < tar:
                low = mid + 1
            else:
                high = mid - 1
        return sol
    
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        f = self.firstOccurence(nums,target,n)
        l = self.lastOccurence(nums,target,n)
        return [f,l]
        