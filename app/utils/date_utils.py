
from datetime import date, datetime, timedelta
import math

# 그 달에 해당되는 분기를 반환
def quarter_year(month):
  return math.ceil( month / 3.0 )

# 년 월 일 date를  Format 00 으로 맞춰 반환
def get_date(y, m, d):
    s = f'{y:04d}-{m:02d}-{d:02d}'
    return s

# 월의 해당 주차를 반환
def get_week_of_month(y, m, d):
    target =  datetime.strptime(get_date(y, m, d), '%Y-%m-%d')
    firstday = target.replace(day=1)
    if firstday.weekday() == 6:
        origin = firstday
    elif firstday.weekday() < 3:
        origin = firstday - timedelta(days=firstday.weekday() + 1)
    else:
        origin = firstday + timedelta(days=6-firstday.weekday())
    return (target - origin).days // 7 + 1


# print(get_date(2020,10,1))
# today = date.today()
# print(today)
# print(today.day)
# print(today.month) 
# quarter_year(today.month)
# print(today.year)
# p = "{}년 {}월 {}일 \n목표 대비 생산현황 입니다".format(today.year, today.month, today.day)
# print(p)
# print(get_date(today.year, today.month, today.day))
# print(get_week_of_month(2021, 1, 30))