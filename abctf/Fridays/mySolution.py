#!/usr/bin/env python
#Author:Aditya kamat

import urllib2 

data = urllib2.urlopen('https://gist.githubusercontent.com/LiamRahav/0cbf82b8bc3a41deafc0403f1b1dd573/raw/cfdd458378bf2da29575f3b275ca343c1ec501bc/date.txt')
month1 = {"January" : '01', "February" : '02', "March" : '03', "April" : '04', "May" : '05', "June" : '06', "July" : '07', "August" : '08', "September" : '09', "October" : '10', "November" : '11', "December" : '12'}  

def weekDay(year, month, day):
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    week   = ['Sunday', 
              'Monday', 
              'Tuesday', 
              'Wednesday', 
              'Thursday',  
              'Friday', 
              'Saturday']
    afterFeb = 1
    if month > 2: afterFeb = 0
    aux = year - 1700 - afterFeb
    # dayOfWeek for 1700/1/1 = 5, Friday
    dayOfWeek  = 5
    # partial sum of days betweem current date and 1700/1/1
    dayOfWeek += (aux + afterFeb) * 365                  
    # leap year correction    
    dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400     
    # sum monthly and day offsets
    dayOfWeek += offset[month - 1] + (day - 1)               
    dayOfWeek %= 7
    return week[dayOfWeek]


count = 0
for i in data:
	i = i.replace(",","")
	date1 = i.split()
	for j in month1.keys():
		if date1[0] in j:
			date1[0] = month1.get(j,"default") 
	date1[2] = int(date1[2]) + 1
	#my_date = int(date1[2])+"-"+int(date1[0])+"-"+int(date1[1])
	#calendar.day_name[my_date.weekday()]
	#print date1
	res = weekDay(int(date1[2]), int(date1[0]), int(date1[1]))	
	if res == "Friday":
		count += 1
	

print count
