import re
import sys
datas=sys.argv[1]
values=[]
with open(datas) as f:
    for data in f:
        data = data.encode("ascii", "ignore").decode()
        data=re.sub('\s+',' ',data)
        #BK101 	1 	1006 	current_timestamp - 8760 hours 	Yonkers 	Brooklyn 	pool 	1 	completed
        #1      2     3                         4            5          6       7   8     9
        pattern=r"^(BK\d*) (\d*) (\d*) current_timestamp[-– ]*(\d* ?\w*) (\w*) (\w*) (\w{4}) (\d*|NULL) (\w*)"
        insert=r'INSERT INTO booking_details VALUES("\1",\2,\3, subtime(current_timestamp(),"\4"),"\5","\6","\7",\8,"\9");'
        values.append(re.sub(pattern,insertis, data))
print('\n'.join(values))
print("\n\nsubtime function has to be edited")

#subtime function has to be edited
"""
BK101 	1 	1006 	current_timestamp - 8760 hours 	Yonkers 	Brooklyn 	pool 	1 	completed
BK102 	2 	1006 	current_timestamp - 8001 hours 	Yonkers 	Brooklyn 	pool 	1 	completed
BK103 	3 	1006 	current_timestamp - 7665 hours 	Yonkers  	Brooklyn 	pool 	2 	completed
BK104 	3 	1001 	current_timestamp - 438000 minutes 	Manhattan 	Queens 	solo 	NULL 	cancelled
BK105 	5 	1003 	current_timestamp - 394300 minutes 	Queens 	Elizabeth 	solo 	3 	completed
BK106 	5 	1004 	current_timestamp - 306199 minutes 	Elizabeth 	Queens 	solo 	1 	completed
BK107 	6 	1005 	current_timestamp - 262000 minutes 	Elizabeth 	Brooklyn 	solo 	NULL 	cancelled
BK108 	3 	1004 	current_timestamp - 175200 minutes 	Elizabeth 	Huntington 	solo 	NULL 	completed
BK109 	4 	1003 	current_timestamp - 100000 minutes 	Huntington 	Woodrow 	solo 	NULL 	cancelled
BK110 	4 	1006 	current_timestamp - 80000 minutes 	Woodrow 	Manhattan 	solo 	NULL 	cancelled
BK111 	1 	1007 	current_timestamp - 40000 minutes 	Queens 	Newark 	solo 	NULL 	completed
BK112 	1 	1008 	current_timestamp - 262800 seconds 	Huntington 	Woodrow 	solo 	NULL 	completed
BK113 	5 	1010 	current_timestamp - 720 seconds 	Huntington 	Manhattan 	solo 	NULL 	waiting
BK114 	4 	1009 	current_timestamp - 360 seconds 	Brooklyn 	Yonkers 	pool 	2 	travelling
BK115 	6 	1009 	current_timestamp 	Brooklyn 	Yonkers 	pool 	4 	travelling
"""

"""
INSERT INTO booking_details VALUES("BK101",1,1006, subtime(current_timestamp(),"8760 hours"),"Yonkers","Brooklyn","pool",1,"completed");
INSERT INTO booking_details VALUES("BK102",2,1006, subtime(current_timestamp(),"8001 hours"),"Yonkers","Brooklyn","pool",1,"completed");
INSERT INTO booking_details VALUES("BK103",3,1006, subtime(current_timestamp(),"7665 hours"),"Yonkers","Brooklyn","pool",2,"completed");
INSERT INTO booking_details VALUES("BK104",3,1001, subtime(current_timestamp(),"438000 minutes"),"Manhattan","Queens","solo",NULL,"cancelled");
INSERT INTO booking_details VALUES("BK105",5,1003, subtime(current_timestamp(),"394300 minutes"),"Queens","Elizabeth","solo",3,"completed");
INSERT INTO booking_details VALUES("BK106",5,1004, subtime(current_timestamp(),"306199 minutes"),"Elizabeth","Queens","solo",1,"completed");
INSERT INTO booking_details VALUES("BK107",6,1005, subtime(current_timestamp(),"262000 minutes"),"Elizabeth","Brooklyn","solo",NULL,"cancelled");
INSERT INTO booking_details VALUES("BK108",3,1004, subtime(current_timestamp(),"175200 minutes"),"Elizabeth","Huntington","solo",NULL,"completed");
INSERT INTO booking_details VALUES("BK109",4,1003, subtime(current_timestamp(),"100000 minutes"),"Huntington","Woodrow","solo",NULL,"cancelled");
INSERT INTO booking_details VALUES("BK110",4,1006, subtime(current_timestamp(),"80000 minutes"),"Woodrow","Manhattan","solo",NULL,"cancelled");
INSERT INTO booking_details VALUES("BK111",1,1007, subtime(current_timestamp(),"40000 minutes"),"Queens","Newark","solo",NULL,"completed");
INSERT INTO booking_details VALUES("BK112",1,1008, subtime(current_timestamp(),"262800 seconds"),"Huntington","Woodrow","solo",NULL,"completed");
INSERT INTO booking_details VALUES("BK113",5,1010, subtime(current_timestamp(),"720 seconds"),"Huntington","Manhattan","solo",NULL,"waiting");
INSERT INTO booking_details VALUES("BK114",4,1009, subtime(current_timestamp(),"360 seconds"),"Brooklyn","Yonkers","pool",2,"travelling");
INSERT INTO booking_details VALUES("BK115",6,1009, subtime(current_timestamp(),""),"Brooklyn","Yonkers","pool",4,"travelling");
"""

