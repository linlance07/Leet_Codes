class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        t = s = st = 0
        for i in range(len(gas)):
            t += gas[i] - cost[i]
            s += gas[i] - cost[i]
            if s<0:
                s = 0
                st = i + 1
        if t>=0:
            return st
        return -1