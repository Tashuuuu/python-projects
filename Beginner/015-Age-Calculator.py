# 8. Age Calculator:
import time
this_year = int(time.strftime("%Y"))
this_month = int(time.strftime("%m"))
this_day = int(time.strftime("%d"))

a = input("Enter your date of birth (DD/MM/YYYY): ")
age = a.split("/")

born_year = int(age[2])
born_month = int(age[1])
born_day = int(age[0])

def year(son):
  p = this_year - (born_year + 1)
  return p
age_year = year(born_year)

def month(born_month):
  q = (12 - born_month) + (this_month - 1)
  return q
age_month = month(born_month)

def day(born_day):
  if (born_month == 1 or born_month == 3 or born_month == 5 or born_month == 7 or born_month == 8 or born_month == 10 or born_month == 12):
    r =  (31 - born_day) + this_day
    return r
  elif (born_month == 4 or born_month == 6 or born_month == 9 or born_month == 11):
    r =  (30 - born_day) + this_day
    return r
  else:
    r = (28 - born_day) + this_day
    return r
age_day = day(born_day)

if age_day >= 93:
  age_month = age_month + 3
  age_day = age_day - 93
elif age_day >= 62:
  age_month = age_month + 2
  age_day = age_day - 62
elif age_day >= 31:
  age_month = age_month + 1
  age_day = age_day - 31

if age_month >= 36:
  age_year = age_year + 3
  age_month = age_month - 36
elif age_month >= 24:
  age_year = age_year + 2
  age_month = age_month - 24
elif age_month >= 12:
  age_year = age_year + 1
  age_month = age_month - 12

print(f"So your age is {age_year} years {age_month} months and {age_day} days.")



