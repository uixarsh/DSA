class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        pref_sum = 0
        freq = {0: 1}

        for ele in nums:
            pref_sum+=ele

            diff = pref_sum - k

            if diff in freq:
                cnt += freq[diff]

            freq[pref_sum] = freq.get(pref_sum, 0) + 1

        return cnt