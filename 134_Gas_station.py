"""
The gas list is a cyclic list. 
In order for traveling a loop, there should be more gas than traveling cost.
Obviously, sum(x,y) = gas(x)- cost(x) + gas(x+1) - cost(x+1) + ....gas(y)-cost(y) >= 0
x,y is the starting and ending point of the cyclic list.
Obviously, in this list, there must exist a sublist (k,y) that sum(k,y) >= 0, the extreme condition is sum(y,y) >= 0
there is one more condition:
sum(k,k) >=0 and all sum(k,j)>=0 for j in between k and y
so just watch out for sum(k,i)<0 then reset k to be i+1
"""


class Solution():
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        balance = 0
        index = 0
        for i in range(n):
            balance += gas[i] - cost[i]
            if balance < 0:
                balance = 0
                index = i+1
        return index

