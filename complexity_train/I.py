from datetime import date, timedelta, datetime

n = int(input())
year = int(input())

start_date = date(year,1,1)
end_date = date(year, 12,31)

wk_cnt = [0 for i in range(7)]

while start_date <= end_date:
    wk_cnt[start_date.weekday()]+=1
    start_date += timedelta(days=1) 

for i in range(n):
    day, month = input().split()
    month = int(datetime.strptime(month, '%B').month)
    wk_cnt[date(year, month, int(day)).weekday()]-=1

useless = input()

mx_ind = 0
for i in range(7):
    if wk_cnt[mx_ind] < wk_cnt[i]:
        mx_ind = i

mi_ind = 0
for i in range(7):
    if wk_cnt[mi_ind] > wk_cnt[i]:
        mi_ind = i


days_names = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday","Sunday"]    

#print(wk_cnt)
print(days_names[mx_ind], days_names[mi_ind])