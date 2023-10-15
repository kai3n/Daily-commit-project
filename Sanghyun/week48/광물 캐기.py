def solution(picks, minerals):
    answer = 0
    count =0
    # 곡괭이 수 저장
    for i in picks:
        count += i
    
    #곡괭이로 캘 수 있는 광물만큼 자름
    num = count * 5
    if len(minerals)>count:
        minerals = minerals[:num]
    
    #다이아몬드, 철, 돌 성분 저장
    new_minerals =[[0,0,0] for _ in range((len(minerals) //5 +1))]
    for i in range(len(minerals)):
        if minerals[i]=='diamond':
            new_minerals[i//5][0]+=1
        elif minerals[i]=='iron':
            new_minerals[i//5][1]+=1
        elif minerals[i]=='stone':
            new_minerals[i//5][2]+=1
    
    #광물의 순서를 다이아몬드, 철, 돌 순서대로 정렬
    new_minerals.sort(key=lambda x:(-x[0],-x[1],-x[2]))
    
    #정렬된 광물들을 다이아,철,돌 곡괭이 순서대로 캠
    for i in new_minerals:
         dia, iron, stone = i
         for j in range(len(picks)):
            # 다이아 곡괭이로 캐므로 그에따라 피로도 갱신
            if picks[j]>0 and j==0:
                picks[j]-=1
                answer += dia + iron + stone
                break
            # 철 곡괭이로 캐므로 그에따라 피로도 갱신 
            elif picks[j]>0 and j==1:
                picks[j]-=1
                answer += (5*dia) + iron + stone
                break
            # 돌 곡괭이로 캐므로 그에따라 피로도 갱신
            elif picks[j]>0 and j==2:
                picks[j]-=1
                answer += (25*dia) + (5*iron) + stone
                break
    # 광물들을 캐는데 최소한의 피로도 반환
    return answer