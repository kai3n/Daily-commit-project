def solution(files):
    # 파일명 정렬시킬곳
    temp = []
    head,number,tail = '','',''
    
    for file in files:
        for idx in range(len(file)):
            # 숫자까지 head이므로 그 뒤로는 number로 저장
            if file[idx].isdigit():
                head = file[:idx]
                number = file[idx:]
                
                for number_idx in range(len(number)):
                    # 숫자가 아니면 뒤에는 tail이므로 따로 저장
                    if not number[number_idx].isdigit():
                        tail = number[number_idx:]
                        number = number[:number_idx]
                        break
                # head, number, tail 로 나눠서 temp에 저장
                temp.append([head,number,tail])
                # head, number, tail 초기화 
                head, number, tail = '', '', ''
                break
    # 소문자기준, 숫자기준으로 정렬 
    answers = sorted(temp, key = lambda x : (x[0].lower(), int(x[1])) )
    # 파일정렬 시켜서 리스트를 문자열로 바꾼 후 반환
    return [''.join(answer) for answer in answers]