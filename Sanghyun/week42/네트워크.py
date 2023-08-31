def solution(n, computers):
    # 방문자 체크 
    visited=[0]*n 
    # 연결 성분 개수
    answer=0 
    # dfs 깊이 계속 탐색
    def dfs(pc): 
        # 방문시 1로 갱신
        visited[pc]=1 
        # 해당 컴퓨터에 연결된 컴퓨터 반복
        for idx,c in enumerate(computers[pc]): 
            if c and visited[idx]==0:
                dfs(idx)
                
    for pc in range(n):      
        # 해당 컴퓨터 방문 안했을 시
        if visited[pc] == 0: 
            dfs(pc)     
            # 연결된 성분 갱신
            answer+=1   
    # 몇개의 네트워크로 연결 되는지 반환
    return answer