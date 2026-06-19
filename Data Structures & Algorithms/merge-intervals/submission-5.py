class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        n, i = len(intervals), 0

        if n == 1:
            return intervals

        intervals.sort(key=lambda pair:pair[0])

        output.append(intervals[0])

        for start, end in intervals:
            if start <= output[-1][1]:
                output[-1][0] = min(output[-1][0], start)
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start,end])
        return output

# 1     3
# <----->
# <----------->
# 1           5
#   1     4
#   <------>
0,0


