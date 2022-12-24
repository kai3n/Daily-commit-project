def solution(record):
    # 아이디별로 닉네임 저장하는 db
    db = {}
    # 들어오거나 나갈때 출력되는 문장 저장
    answer = []
    # 저장된 행위에 대해 반복 
    for user in record:
        # 공백 기준으로 리스트변환 
        user_list = user.split(' ')
        # Enter 또는 Change 가 들어오면 db에서 키는 아이디를 기준으로 값은 닉네임으로 갱신 
        if user_list[0] == "Enter" or user_list[0] == "Change":
            db[user_list[1]] = user_list[2]
    # 저장된 행위에 대해 반복
    for item in record:
        # 문장 초기화
        temp = ''
        # 공백을 기준으로 리스트 변환
        item_list = item.split(' ')
        # Enter 가 들어왔을때
        if item_list[0] == "Enter":
            # db에서 키값을 찾아서 닉네임 반환
            user = db[item_list[1]]
            # 문장 저장 후 answer리스트에 추가 
            temp = f"{user}님이 들어왔습니다."
            answer.append(temp)
        # Leave는 나갔을때
        elif item_list[0] == "Leave":
            # db에 잇는 닉네임 반환 
            user = db[item_list[1]]
            # 문장 저장 후 answer리스트에 추가 
            temp = f"{user}님이 나갔습니다."
            answer.append(temp)
    # 어떤 닉네임이 들어오고 나갔는지 리스트로 반환
    return answer