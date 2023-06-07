def solution(number, limit, power):
    #철의 무게가 얼마나 필요한지 반환
    answer = 0
    for i in range(1,number+1):
        count=0
        for j in range(1,int(i**(1/2)+1)):
            # i숫자 약수갯수 출력
            if i%j==0:
                count+=1
                if j**2!=i:
                    count+=1
        # 약수 갯수가 limit보다 작으면 그대로 더해서 저장
        if count <=limit:
            answer+=count
        # 약수 갯수가 limit보다 크면 power을 더해서 저장
        else:
            answer+=power
    # 철의 무게 반환
    return answer