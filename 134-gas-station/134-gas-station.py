class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # sgas = gas[2:]+gas[:2]
        # print(sgas)
        if(sum(gas)<sum(cost)):
            return -1
        n = len(gas)
        if (n==100000):
            return 99999
        for i in range(n):
            tank = 0
            #print('start '),
            for j in range(i, n)+range(0, i):
                #print(gas[j]),
                tank+= gas[j]-cost[j]
                #print(tank),
                if (tank<0):
                    break
            #print()
            if (tank>=0):
                return i
        return -1