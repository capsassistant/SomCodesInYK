import re
import sys
datas=sys.argv[1]
values=[]
with open(datas) as f:
    for data in f:
        data = data.encode("ascii", "ignore").decode()
        data=re.sub('\s+',' ',data)
        pattern=r"^(\d*) (\w* \w*) current_date [-– ]*(\d*) days (\d{10}) (\w*) (\d*) ([\d\.])*$"
        insert=r"INSERT INTO customer_details VALUES(\1,'\2',date_sub(curdate(),interval \3 day),\4,'\5','\6');"
        values.append(re.sub(pattern,insert, data))
print('\n'.join(values))
        
        
#1 	Ted Moseby 	current_date – 100 days 	9898989898 	Manhattan 	110 	400.00
#1     2                   3                 4            5         6      7
"""
1 	Ted Moseby 	current_date – 100 days 	9898989898 	Manhattan 	110 	400.00
2 	Sheldon Copper 	current_date – 90 days 	8989898989 	Queens 	230 	150.00
3 	Jessy Pinkman 	current_date – 80 days 	7878787878 	Pomonok 	80 	346.00
4 	Billy Kimber 	current_date – 75 days 	8787878787 	Brooklyn 	90 	499.00
5 	Thomas Shelby 	current_date – 40 days 	9090909090 	Newark 	30 	341.00
6 	John Snow 	current_date – 20 days 	8908908908 	Yonkers 	50 	267.00
"""

"""
INSERT INTO customer_details VALUES(1,'Ted Moseby',date_sub(curdate(),interval 100 day),9898989898,'Manhattan','110');
INSERT INTO customer_details VALUES(2,'Sheldon Copper',date_sub(curdate(),interval 90 day),8989898989,'Queens','230');
INSERT INTO customer_details VALUES(3,'Jessy Pinkman',date_sub(curdate(),interval 80 day),7878787878,'Pomonok','80');
INSERT INTO customer_details VALUES(4,'Billy Kimber',date_sub(curdate(),interval 75 day),8787878787,'Brooklyn','90');
INSERT INTO customer_details VALUES(5,'Thomas Shelby',date_sub(curdate(),interval 40 day),9090909090,'Newark','30');
INSERT INTO customer_details VALUES(6,'John Snow',date_sub(curdate(),interval 20 day),8908908908,'Yonkers','50');
"""
