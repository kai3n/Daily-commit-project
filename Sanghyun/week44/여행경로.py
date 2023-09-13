import collections

answer = []
graph = collections.defaultdict(list)

def dfs(s):
    # 키 값이 있으면 빼서 계속 탐색
    while graph[s]:
        dfs(graph[s].pop(0))
    # 키 값이 없으면 결과값에 저장
    if not graph[s]:
        answer.append(s)
        return

def solution(tickets):
    # 출발지 도착지를 딕셔너리로 저장
    for a,b in tickets:
        graph[a].append(b)
    # 알바펫 순서가 같을 경우 대비해서 정렬
    for a, b in graph.items():
        graph[a].sort()
    # ICN 탐색시작
    dfs("ICN")
    # 뒤집어서 공항 경로 반환
    return answer[::-1]