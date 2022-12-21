def solution(numbers, target):
    # 몇가지 방법 있는지 저장
    answer = 0
    # 모든경우의수 다 담을 공간
    store = [0]
    # 리스트 반복
    for num in numbers:
        # num에 대해서 경우의수 저장공건
        temp = []
        # store에 있는만큼 반복
        for item in store:
            # store에 잇는 모든 경우의수를 num만큼 뺴고 더한 값들 저장
            temp.append(item + num)
            temp.append(item - num)
        # temp에 저장 된 리스트들 다시 store에 저장 
        store = temp
    # +, - 한 모두의 경우중에서 target값만 같을때 +1 갱신 
    for count in store:
        if count == target:
            answer += 1
    # +, - 해서 타겟값 만들수 있는 모든 방법의 수 반환
    return answer