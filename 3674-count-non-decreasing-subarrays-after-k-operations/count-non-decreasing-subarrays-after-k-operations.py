class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = opr = left = 0
        q = []
        st = []
        pos = [n] * n
        cnt = [[] for _ in range(n)]

        for right in range(n):
            while st and nums[right] >= nums[st[-1]]:
                pos[st[-1]] = right
                st.pop()
            if st:
                cnt[st[-1]].append(right)
            st.append(right)
            heapq.heappush(q, (-nums[right], right))
            opr += max(0, -q[0][0] - nums[right])
            while opr > k:
                for i in cnt[left]:
                    opr -= (nums[left] - nums[i]) * (
                        min(pos[i], right + 1) - i
                    )
                left += 1
            while q and q[0][1] < left:
                heapq.heappop(q)
            ans += right - left + 1
        return ans
        