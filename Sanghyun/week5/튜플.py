def solution(s):
    # s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    answer = []
    # 문자열에서 {{ ,}} 부분을 먼저 짤라서 new_s에 저장 
    new_s = s[2:-2]
    # new_s에서 },{ 이 단위로 짤라서 리스트에 저장 
    new_s_list = new_s.split('},{')
    # 길이를 기준으로 정렬 
    new_s_list.sort(key=len)
    # new_s_list갯수만큼 반복
    for item in new_s_list:
        # item은 아직 문자열이므로 ,기준으로 리스트로 변환 
        item_list = item.split(',')
        # item_list갯수만큼 반복
        for v in item_list:
            # 만약에 answer안에 v값이 없다면 추가 
            if int(v) not in answer:
                answer.append(int(v))
    # 중복되는 원소가 없는 값들 반환 
    return answer