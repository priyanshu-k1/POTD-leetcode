class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            prod = nums[i]
            gcdVal = nums[i]
            lcmVal = nums[i]
            for j in range(i + 1, len(nums)):
                prod = prod * nums[j]
                gcdVal = gcd(gcdVal, nums[j])
                lcmVal = lcm(lcmVal, nums[j])
                if prod > gcdVal * lcmVal:
                    break
                if prod == gcdVal * lcmVal:
                    ans = max(ans, j - i + 1)
        return ans