def solution(arr, k):
    store = []
    for i in arr:
        # store에 없으면 저장
        if i not in store:
            store.append(i)
        # store의 개수가 k랑 같을떄 중지
        if len(store) == k:
            break
    # store에 중복말고 저장할게 없으면 -1로 저장후 반환
    return store + [-1] * (k - len(store))