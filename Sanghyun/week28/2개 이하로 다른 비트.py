def solution(numbers):
    answer = []

    for number in numbers :
        # 짝수 일때는 마지막비트에 +1 더함 
        if number%2==0:
            answer.append(number+1)
            continue
        # 홀수 일때 맨앞에 0을 추가함 
        num_to_bin= '0' + bin(number)[2:]
        # 01 과 10을 바꿔서 처리함 
        num_to_bin = num_to_bin[:num_to_bin.rindex('0')] + '10' + num_to_bin[num_to_bin.rindex('0') + 2:]
        # 2진법으로 바꾼후 저장
        answer.append(int(num_to_bin, 2))
    # 자신보다는 큰 2개 이하로 다른 비트 반환
    return answer