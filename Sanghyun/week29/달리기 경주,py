def solution(players, callings):
    # 두개 딕셔너리로 구성 
    main_dict = {rank : player for rank , player in enumerate(players)}
    sub_dict = {player : rank for rank , player in enumerate(players)}
    # 심판이 부르면 선수가 추월하므로 딕셔너리 값 갱신 
    for player in callings:
        # 현재 등수 
        rank = sub_dict[player]
        # 현재등수보다 높은 등수 
        high_rank = rank-1
        # 추월 당할 선수이름 
        high_rank_player = main_dict[high_rank]
        # player의 등수를 바꾸고, 추월 당할 선수의 등수를 떨어트림
        main_dict[rank-1] = player
        main_dict[rank] = high_rank_player
        # 선수들의 등수를 바꿔줌
        sub_dict[player] = high_rank
        sub_dict[high_rank_player] = rank
    # 최종 목적지에 등수 순서로 선수이름 반환
    return list(main_dict.values())