class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i, n = 0, len(intervals)

        while i<n and intervals[i][1]<newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        x, y = newInterval[0], newInterval[1]
        while i<n and intervals[i][0] <= y:
            x = min(intervals[i][0], x)
            y = max(intervals[i][1], y)
            i += 1
        result.append([x,y])

        while i<n:
            result.append(intervals[i])
            i+=1 
        
        return result