from collections import defaultdict

def solution(genres, plays):
    answer = []
    play_dict = defaultdict(int)
    # 장르,재생횟수,고유번호 순으로 저장
    temps = [[genres[i],plays[i],i] for i in range(len(genres))]
    # 장르별, 재생횟수가 많을수록, 고유번호가 작을수록 기준으로 정렬 
    temps = sorted(temps, key = lambda x : (x[0],-x[1],x[2]))
    # 장르별 총 몇번 재생됬는지 저장
    for i in range(len(genres)):
        play_dict[genres[i]] += plays[i]
    # 재생횟수가 많을수록 기준으로 정렬
    play_dict = sorted(play_dict.items(), key = lambda x : -x[1])
    
    for genre in play_dict:
        # 최대 2개만 저장하기위해 카운트
        count = 0
        for temp in temps:
            # 장르가 같으면 count갱신 
            if genre[0] == temp[0]:
                count +=1
                # 최대 두개만저장
                if count > 2:
                    break
                else:
                    answer.append(temp[2])
    # 재생횟수가 많은 장르중에 최대 2개 재생횟수 고유번호 반환
    return answer