def solution(arr, query):
    # 쿼리 수만큼 반복
    for i in range(len(query)):
        # 짝수일때 뒷부분 짜름
        if i % 2 == 0 :
            arr = arr[:query[i]+1]
        # 홀수일때 앞부분 짜름
        else :
            arr = arr[query[i]:]
    # 작업을 다 끝낸후 반환
    return arr