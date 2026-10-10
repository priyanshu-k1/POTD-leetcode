class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        k = k1 + k2
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        max_diff = max(diffs)
        
        if max_diff == 0:
            return 0
        buckets = [0] * (max_diff + 1)
        for d in diffs:
            buckets[d] += 1
        for d in range(max_diff, 0, -1):
            if buckets[d] == 0:
                continue
                
            count = buckets[d]
            ops_needed = count
            
            if k >= ops_needed:
                buckets[d - 1] += count
                buckets[d] = 0
                k -= ops_needed
            else:
                buckets[d - 1] += k
                buckets[d] -= k
                k = 0
                break
        ans = 0
        for d in range(1, max_diff + 1):
            if buckets[d] > 0:
                ans += buckets[d] * (d ** 2)
                
        return ans
        