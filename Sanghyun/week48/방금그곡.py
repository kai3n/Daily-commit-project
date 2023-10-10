def solution(m, musicinfos):
    # 높은 음은 소문자로 전환
    def change(music):
        if 'A#' in music:
            music = music.replace('A#', 'a')
        if 'F#' in music:
            music = music.replace('F#', 'f')
        if 'C#' in music:
            music = music.replace('C#', 'c')
        if 'G#' in music:
            music = music.replace('G#', 'g')
        if 'D#' in music:
            music = music.replace('D#', 'd')
        return music
    
    check = []
    for i, musicinfo in enumerate(musicinfos):
        # 재생시간에 총 악보 저장
        ackbo = ''
        # 곡에 대한 정보 ,기준으로 리스트
        list_musicinfo = musicinfo.split(',')
        # 재생 시작시간
        start_minute = int(list_musicinfo[0][0:2]) * 60 + int(list_musicinfo[0][3:5])
        # 재생 종료시간
        end_minute = int(list_musicinfo[1][0:2]) * 60 + int(list_musicinfo[1][3:5])
        # 총 플레이 시간
        play_minute = end_minute - start_minute
        # 높은음은 전부 소문자로 바꿔 한개음으로 분류 
        change_ackbo = change(list_musicinfo[3])

        for j in range(play_minute):
            # ackbo에 재생시간 만큼 계속 음들 저장
            ackbo += change_ackbo[j%len(change_ackbo)]
        # 내가 들은 곡 높음은을 소문자로 바꿔 한개음으로 변경
        changd_m = change(m)
        # 재생길이, 곡이름, 먼저 듣는 순서대로 리스트에 저장
        if changd_m in ackbo:
            check.append((play_minute,list_musicinfo[2],i))
    # 재생시간이 길수록, 재생시간이 같으면 먼저 들은순서대로 정렬
    check.sort(key = lambda x :(-x[0],x[2]))
    # check에 있으면 곡이름 반환
    if check:
        return check[0][1]
    # 곡이 없으므로 None반환
    return '(None)'