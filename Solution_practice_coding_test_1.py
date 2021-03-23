
def solution(participant, completion):

    # 동명이인이 없는 경우 set함수로 중복제거
    comp = list(set(participant) - set(completion))

    # 동명이인이 0일경우 그값을 출력해준다.(동명이인이 아닌사람)
    if len(comp) != 0:
        return comp[0]

    # 동명이인이 있는 경우 정렬을 해준다.
    participant = sorted(participant)
    completion = sorted(completion)

    for i in range(len(participant)):
        print(participant[i])
        #각인덱스가 달랐을때 동명이인이 발생되었을때 출력해준다.
        if participant[i] != completion[i]:
            return participant[i]
        print(participant[i])
    answer = ''
    print("return answer : {}".format(answer))
    return answer


if __name__ == '__main__':
    #print('run main!!')
    participant, participant2 = ['leo', 'kiki', 'eden'], ["marina", "josipa", "nikola", "vinko", "filipa"]
    completion, completion2 = ['eden', 'kiki'], ["josipa", "filipa", "marina", "nikola"]

    assert solution(participant, completion) == 'leo'
    assert solution(participant2, completion2) == "vinko"

