import re
import sys


datas=sys.argv[1]
values=[]
with open(datas) as f:
for data in f:
data = data.encode("ascii", "ignore").decode()
data=re.sub('\s+',' ',data)
pattern=r"^([\w]*[\d]*) current_date [-–. ]* ([\d]*) days ([\w ]*) (\d*)$"
insertis=r"INSERT INTO coupon_details VALUES('\1',date_sub(curdate(),interval \2 day),'\3',\4),"
values.append(re.sub(pattern,insertis, data))

with open("newdata.txt", "w") as file:
for value in values:
file.write(value)
