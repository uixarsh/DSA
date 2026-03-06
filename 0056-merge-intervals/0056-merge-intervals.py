class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        rslt = []

        for interval in intervals:
            if not rslt:
                rslt.append(interval)

            last_interval = rslt[-1]

            curr_start = interval[0]
            curr_end = interval[1]
            last_end = last_interval[1]

            if curr_start <= last_end:
                last_end = max(last_end, curr_end)
                last_interval[1] = last_end
                continue
            
            rslt.append(interval)

        return rslt