"""     
   2.      5.
   <------------------>
<----->       <---->         
1.   3.  4.    6


1. newInterval starts after interval ends. 
2. newInterval ends before interval starts.
3. merge case

"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:  
        n, res = len(intervals), []
        i = 0

        # 1. newInterval starts after intervals
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
            print(res)

            # stop when new interval ends after current interval starts

        # 2. newInterval overlaps when new interval 
        while i < n and newInterval[1] >= intervals[i][0] :
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        res.append(newInterval)

        # 3. newInterval ends before interval start
        while i < n:
            res.append(intervals[i])
            i += 1
        return res



        
      


    

#     2.    4
#     <----->  
# <---> <------>
# 1.  2 3.     5




# i : 0
#    (1-->3).  
