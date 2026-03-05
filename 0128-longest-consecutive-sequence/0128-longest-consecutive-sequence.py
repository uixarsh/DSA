class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        longest = 0

        for ele in st:

            # start of sequence
            if (ele - 1) not in st:

                curr = ele
                curr_cnt = 1

                while (curr + 1) in st:
                    curr += 1
                    curr_cnt += 1

                longest = max(longest, curr_cnt)

        return longest