# At First Not Consider Leap Year

days_of_month_arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTH_NUM_PER_YEAR = 12
DAYS_NUM_PER_WEEK = 7
FRIDAY_IDX = 4
# day idx: Mo:0,Tu:1,We:2,Th:3,Fr:4,
sum_of_thirteen_friday = 0

days_left = 0
year = 2007

def get_days_of_month(year,month_idx):
  if month_idx == 1 and year % 4 == 0:
    return 29
  return days_of_month_arr[month_idx]

first_day = 6

while True:
  for i in range(1, MONTH_NUM_PER_YEAR+1):
    days_of_month = get_days_of_month(year,i-1)
    for j in range(1,days_of_month+1):
        if (days_left + first_day) % DAYS_NUM_PER_WEEK == FRIDAY_IDX and j == 13:
                sum_of_thirteen_friday += 1
                print(year,i,j)
                if sum_of_thirteen_friday == 666:
                  print(year,i,j)
                  exit(0)
        days_left += 1
  year += 1

# print(sum_of_thirteen_friday)