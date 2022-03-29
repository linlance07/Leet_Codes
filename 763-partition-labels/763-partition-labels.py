class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        intervals = {}
        for i in range(len(s)):
            currentChar = s[i]
            if currentChar in intervals:
                intervals[currentChar][1] = i
            else:
                intervals[currentChar] = [i,i]
        # extract the intervals
        intervalsList = []
        for index, item in intervals.items():
            intervalsList.append(item)
        intervalsList.sort()
        mergedList = self.mergeIntervals(intervalsList)
        return [y - x + 1 for x,y in mergedList]
    
    # overlapping intervals merge    
    def mergeIntervals(self, listOfIntervals):
        mergedIntervals = []
        left = 0
        right = 1
        while right < len(listOfIntervals):
            if listOfIntervals[left][1] > listOfIntervals[right][0]:
                listOfIntervals[left][1] = max(listOfIntervals[left][1],listOfIntervals[right][1])
                right+=1
            else:
                mergedIntervals.append(listOfIntervals[left])
                left=right
                right+=1
        mergedIntervals.append(listOfIntervals[left])
        return mergedIntervals