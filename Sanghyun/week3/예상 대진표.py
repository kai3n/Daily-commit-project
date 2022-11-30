def solution(n,a,b):
    # a,b에서 몇번째에 경기하게 되는지 저장
    count=0
    while True:
        # example a가 4, b가 7 일경우 a는 첫번째 경기에서 이기면 2번이 되고 b 4번이됨 
        a= (a//2)+(a%2)
        b= (b//2)+(b%2)
        # 서로 경기 한번씩 했으므로 count 갱신 
        count+=1
        # a==b가 같아질때 서로 경기하게 되니깐 break
        if a==b:
            break
    # a,b가 몇번째 경기하는지 반환
    return count