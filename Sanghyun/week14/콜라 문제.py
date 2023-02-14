def solution(a, b, n):
    # 총 몇개의 콜라를 받을수 있는지 반환
    count = 0 
    # n보다 작거나 같으면 반복 
    while a<=n:
        # 나눈 몫에다가 b를 곱해서 몇개인지 저장 
        count += (n//a)*b
        # 빈병 주고 새로운 콜라 받은후 총 가지고있는 콜라 병 갱신 
        n = (n//a)*b+(n%a)
    # 총 몇개 콜라를 받았는지 반환
    return count