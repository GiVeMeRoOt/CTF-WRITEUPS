#!/usr/bin/env python
#Author:Aditya kamat

import urllib2 


data = urllib2.urlopen('https://gist.githubusercontent.com/LiamRahav/0cbf82b8bc3a41deafc0403f1b1dd573/raw/cfdd458378bf2da29575f3b275ca343c1ec501bc/date.txt')

month1 = {"January" : '01', "February" : '02', "March" : '03', "April" : '04', "May" : '05', "June" : '06', "July" : '07', "August" : '08', "September" : '09', "October" : '10', "November" : '11', "December" : '12'}  


days =[ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
       'Sunday' ]
count = 0

def datetoday(day, month, year):
    d = day
    m = month
    y = year
    if m < 3:
        z = y-1
    else:
        z = y
    dayofweek = ( 23*m//9 + d + 4 + y + z//4 - z//100 + z//400 )
    if m >= 3:
        dayofweek -= 2
    dayofweek = dayofweek%7
    return dayofweek



for i in data:
	i = i.replace(",","")
	date1 = i.split()
	for j in month1.keys():
		if date1[0] in j:
			date1[0] = month1.get(j,"default") 
	date1[2] = int(date1[2]) + 1
	dayofweek = days[datetoday(int(date1[1]), int(date1[0]), int(date1[2]))-1]

	print dayofweek	
	if dayofweek == "Friday":
		count += 1
	

print count
