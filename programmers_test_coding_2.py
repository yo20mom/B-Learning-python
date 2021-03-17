from datetime import date, timedelta
import datetime


# [브론즈 기간, 실버 기간, 골드 기간, 플래티넘 기간, 다이아몬드 기간] 순서로 채워서 반환

# required fuc
# 1. full date를 넣으면 day로 환산한 일자를 반환
# 2. grade를 계산

def convert_date_to_day():
    pass


def calc_grade():
    pass


def enrich_info(params):
    result = []
    for x in params:
        temp_date = date.fromisoformat(x.split()[0].replace('/', '-'))
        init_date = date.strftime(temp_date, '%Y/%m/%d')
        result.append({
            'init': init_date,
            'price': x.split()[1],
            'expire': date.strftime(temp_date + timedelta(days=30), '%Y/%m/%d')
        })

    print(result)
    return result


def solution(purchase):
    answer = []
    # insert expire date, init date, payment_money
    grade_info = enrich_info(purchase)

    return answer


if __name__ == '__main__':
    print(solution(
        ["2019/01/30 5000", "2019/04/05 10000", "2019/06/10 20000", "2019/08/15 50000", "2019/12/01 100000"]) == [
              245, 30, 30, 30, 30])
