# 문자 입력
s = input()
# alpha 리스트에 저장 
alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in alpha:
    # 반복하면서 s문자에서 알파벳 있나 찾음, 없으면 -1반환
    print(s.find(i), end =' ')