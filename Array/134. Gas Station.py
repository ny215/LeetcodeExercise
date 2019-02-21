class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        minGas = 0
        minGasLoc = None
        for i in range(len(gas)):
            tank += gas[i]
            tank -= cost[i]
            if tank < minGas:
                minGas = tank
                minGasLoc = i
        if minGasLoc is None:
             return 0
        return minGasLoc+1
            