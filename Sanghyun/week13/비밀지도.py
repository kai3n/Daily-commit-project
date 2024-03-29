def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        # 두 지도 합치기 
        answer.append(bin(arr1[i] | arr2[i])[2:].zfill(n))
        # 0을 공백으로 치환
        answer[i] = answer[i].replace('0', ' ')	
        # 1을 벽으로 치환
        answer[i] = answer[i].replace('1', '#')	
        
    return answer