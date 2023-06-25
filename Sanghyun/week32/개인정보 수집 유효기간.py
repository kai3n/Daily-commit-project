
def solution(today, terms, privacies):
    terms_key = {}
    answer = []
    # 유효기간 타입, 기간 저장
    for item in terms:
        item = item.split()
        terms_key[item[0]] = int(item[1]) * 28

    for idx , date in enumerate(privacies):
        # 유효기간 타입
        terms_type = date[-1]
        date = date[:11].split('.')
        # 년 월 일을 다 일로 바꿔서 계산
        total_day =  int(date[0]) * 12 * 28 + int(date[1])* 28 +int(date[2])+ int(terms_key[terms_type])

        todays = today.split('.')
        # 오늘 날짜 기준으로 다 일로 바꿔서 계산
        total_today = int(todays[0]) * 12 * 28 + int(todays[1])* 28 +int(todays[2]) 
        # 유효기간이 지나면 파기해야 되므로 answer에 인덱스 추가
        if total_day <= total_today:
            answer.append(idx+1)
    # 유효기간 파기 해야할 인덱스 번호 반환
    return answer