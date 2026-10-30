class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        net_gas = 0
        curr_gas = 0
        start = 0
        for i in range(n):
            curr_gas += gas[i] - cost[i]
            net_gas += gas[i] - cost[i]

            if curr_gas < 0:
                curr_gas = 0
                start = i + 1

        return start if net_gas >= 0 else -1