import collections
def solution(progresses, speeds):
    answer = []

    progresses = collections.deque(progresses)
    speeds = collections.deque(speeds)

    while len(progresses):
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while len(progresses):
            if progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                cnt += 1
            else:
                break
        if cnt > 0:
            answer.append(cnt)


    return answer