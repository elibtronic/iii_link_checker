
import urllib2
from random import randint
from time import sleep

report = open("report.csv","w+")

prog = 1

for line in open("out.txt"):
	url_check = line.split(",")
	req = urllib2.Request(url_check[1].strip(" "))
	try:
		resp = urllib2.urlopen(req)
	except urllib2.HTTPError as e:
		report.write(str(e.code)+","+str(line))
		report.flush()
	else:
		report.write(str(resp.getcode())+","+str(line))
		report.flush()
	print prog
	prog += 1
	sleep(randint(1,5)) #Take it easy on requests
