def solution(rows, columns, queries):
    # 최소값 담을 리스트 
    answer = []
    # 행렬 초기화 
    matrix = []
    # rows * columns 행렬 초기화 
    for i in range(rows):
        table = []
        for j in range(i*columns+1,(i+1)*columns+1):
            table.append(j)
        matrix.append(table)
    # querie = [x1,y1,x2,y2]
    for querie in queries:
        # 인덱스에 맞게 갱신 
        querie = [x-1 for x in querie]
        # 한개값은 없어지므로 미리저장 
        temp = matrix[querie[0]][querie[1]]
        # 위치변경된 행렬 최소값 저장
        small = temp 
        # 맨 왼쪽 위로 옮기고 최소값 갱신 
        for i in range(querie[0]+1,querie[2]+1):
            matrix[i-1][querie[1]] = matrix[i][querie[1]]
            small = min(small, matrix[i][querie[1]])
        # 맨 아래 쪽 왼쪽으로 옮기고 최소값 갱신
        for i in range(querie[1]+1,querie[3]+1):
            matrix[querie[2]][i-1] = matrix[querie[2]][i]
            small = min(small, matrix[querie[2]][i])
        # 맨 오른쪽 아래쪽으로 옮기고 최소값 갱신
        for i in range(querie[2]-1,querie[0]-1,-1):
            matrix[i+1][querie[3]] = matrix[i][querie[3]]
            small = min(small, matrix[i][querie[3]])
        # 맨 위쪽 오른쪽으로 옮기고 최소값 갱신 
        for i in range(querie[3]-1,querie[1]-1,-1):
            matrix[querie[0]][i+1] = matrix[querie[0]][i]
            small = min(small, matrix[querie[0]][i])
        # x1,y1값은 없어지므로 미리 저장한곳에서 값 채워주면서 시계방향으로 횐전 
        matrix[querie[0]][querie[1]+1] = temp
        # 위치변경 된 후 최소값 저장
        answer.append(small)
    # querie마다 위치변경 후 최소값들 반환
    return answer