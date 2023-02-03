from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 거리보다 가스가 더 작으면 출발점이 존재하지 않으므로 -1 반환 
        if sum(gas) < sum(cost):
            return -1 
        # start로 출발점 지장 , fuel 연료 갱신 
        start, fuel = 0,0
        # 가스 갯수만큼 반복 
        for i in range(len(gas)):
            # 기름과 남아있는 연료가 cost값 보다 작을시에는 출발점 index + 1 해서 저장 
            if gas[i] + fuel < cost[i]:
                start = i + 1 
                fuel = 0
            # 남아있는 연료 갱신 
            else:
                fuel += gas[i] - cost[i]
        # 경유지를 다 돌기위해서 출발해야할 출발점 반환
        return start