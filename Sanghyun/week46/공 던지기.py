def solution(numbers, k):
    # 2번씩 건너서 k번쨰로 공을 던진 사람 번호 반환
    return numbers[2 * (k - 1) % len(numbers)]