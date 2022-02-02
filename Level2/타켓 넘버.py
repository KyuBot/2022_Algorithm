def solution(numbers, target):
    answer = 0
    def goPlus(idx, result):
        nonlocal numbers
        nonlocal target
        nonlocal answer
        if idx == len(numbers):
            if result == target:
                answer += 1
            return
        goPlus(idx + 1, result + numbers[idx])
        goPlus(idx + 1, result - numbers[idx])

    goPlus(0, 0)

    return answer