from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 반드시 한군데만 존재하므로 cost가 더 클 경우 -1리턴
        if sum(gas) < sum(cost):
            return -1 
        
        start, fuel = 0,0
        for i in range(len(gas)):
            # 해당 인덱스에서 얻은 가스와 기존 가스보다 이동비용이 크면 해당 인덱스는 모두 방문할수 없으므로 start인덱스 갱신
            if gas[i] + fuel < cost[i]:
                start = i + 1 
                fuel = 0
            # 다음 인덱스 계속 체크 
            else:
                fuel += gas[i] - cost[i]
        # 모두 방문할수 있는 출발점 인덱스 반환
        return start 