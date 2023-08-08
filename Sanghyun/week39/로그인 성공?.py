def solution(id_pw, db):
    for i in db:
        # id 여부 체크
        if id_pw[0] in i:
            # 비번 여부 체크
            if id_pw[1] == i[1]:
                # 로그인 성공시 반환
                return "login"
            else:
                # 로그인 비밀번호 실패시 반환
                return "wrong pw"
    # 로그인 실패시 반환
    return "fail"