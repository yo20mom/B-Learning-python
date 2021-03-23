import copy


def add_score(scores):
    """
    등수 추가
    90점 => 1등
    80점 => 2등 ...
    """

    # array를 복사
    temp_scores = copy.deepcopy(scores)

    sorted_temp_list = sorted(temp_scores, reverse=True)
    result_map = {}

    for i, x in enumerate(sorted_temp_list, start=1):
        result_map[x] = i

    print(result_map) #{90: 1, 80: 2, 70: 3, 65: 4, 50: 5} {60: 1, 50: 2, 40: 3, 30: 4, 20: 5}
    return result_map


def solution(math_scores, english_scores):
    answer = 0
    #print(math_scores, english_scores) #[70, 65, 90, 80, 50] [40, 20, 30, 60, 50]
    #     등수 추가
    assert len(math_scores) == len(english_scores)
    #print(math_scores, english_scores)
    temp_math = add_score(math_scores)
    temp_english = add_score(english_scores)

    for i in range(len(math_scores)):
        # A학생 등수를 꺼내옴

        a_math_score = temp_math[math_scores[i]]
        a_english_score = temp_english[english_scores[i]]
        #print(a_math_score,a_english_score)
        for j in range(len(english_scores)):
            # B학생 등수를 꺼내옴
            b_math_score = temp_math[math_scores[j]]
            b_english_score = temp_english[english_scores[j]]
            #print(b_math_score, b_english_score)
            if a_math_score < b_math_score and a_english_score < b_english_score:
                answer += 1
    print(answer)
    return answer


if __name__ == '__main__':
    assert solution([70, 65, 90, 80, 50], [40, 20, 30, 60, 50]) == 5
