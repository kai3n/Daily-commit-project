def solution(numbers, hand):
    answer = ''
	
    #키패드 위치 저장
    table = {'1':(0,0), '2':(0,1), '3':(0,2),
           '4':(1,0), '5':(1,1), '6':(1,2),
           '7':(2,0), '8':(2,1), '9':(2,2),
           '*':(3,0), '0':(3,1), '#':(3,2)
        }
    # 왼손, 오른손 위치 저장
    left = table['*'] 
    right = table['#'] 
    
    for num in numbers :
    	#왼손으로 누르면 저장
        if num == 1 or num == 4 or num == 7 :
            answer += 'L'  
            #해당 번호를 눌렀을 때 왼손의 위치 저장
            left = table[str(num)]
        
        #오른손이 누르면 저장
        elif num == 3 or num == 6 or num == 9 :
            answer += 'R'       
            #해당 번호를 눌렀을 때 오른손의 위치 저장
            right = table[str(num)]   
        
        else :
        	#번호와 왼손의 거리 계산
            left_length = abs(left[0] - table[str(num)][0]) + table(left[1] - table[str(num)][1])
            #번호와 오른손의 거리 계산
            right_length = abs(right[0] - table[str(num)][0]) + table(right[1] - table[str(num)][1])
            
            #왼손이 더 가까울 때 왼손으로 누름
            if left_length < right_length :
                answer += 'L'
                left = table[str(num)]
            
            #오른손이 더 가까울 때 오른손으로 누름
            elif left_length > right_length :
                answer += 'R'
                right = table[str(num)]
            
            #왼손과 오른손 거리가 같을 때 손잡이에 따라 나뉨
            else :
                if hand == 'right' :
                    answer += 'R'
                    right = table[str(num)]
                else :
                    answer += 'L'
                    left = table[str(num)]
    #키패드를 누를때 무슨손으로 누르는지 반환
    return answer