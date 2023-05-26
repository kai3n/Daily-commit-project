def solution(number, k):
    stack = []

    for i in number:
        # k가 0보다크고 스택에서 마지막 값이 i보다 작으면 stack에서 값을빼고 k값 갱신 
        while k > 0 and stack and stack[-1] < i:
            stack.pop()
            k -= 1
        stack.append(i)
    # 숫자가 내림차순 일 경우는 stack의 길이에서 k값을 뺀 길이만 반환
    return ''.join(stack[:len(stack) - k])