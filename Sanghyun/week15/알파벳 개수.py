# 알파벳 입력
str=input()
# 알파벳 갯수만큼 초기화 
count=[0]*26
# str만큼 반복 
for i in str:
    # -97해서 count와 index를 맞춰주고 키 값이있으면 갱신 
    count[ord(i)-97]+=1
# count 출력 
print(*count)