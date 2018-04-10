
import urllib2
import socket
import os.path
import datetime
from random import randint
from time import sleep



def check_url(url_input):
	url_check = url_input.split(",")
	req = urllib2.Request(url_check[1].strip(" "))
	try:
		resp = urllib2.urlopen(req,timeout = 5)
	
	except urllib2.HTTPError as e:
		report.write(datetime.datetime.now().strftime("%d-%m-%Y")+","+str(e.code)+","+str(url_input))
		report.flush()
		print prog,",",str(e.code)+","+str(url_input)

	except:
		report.write(datetime.datetime.now().strftime("%d-%m-%Y")+","+"TIMEOUT,"+str(url_input))
		report.flush()
		print prog,",TIMEOUT,"+str(url_input)
	
	else:
		if str(resp.getcode()) != "200":
			report.write(datetime.datetime.now().strftime("%d-%m-%Y")+","+str(resp.getcode())+","+str(url_input))
			report.flush()
		print prog,",",str(resp.getcode())+","+str(url_input),



if __name__ == "__main__":

	prog = 0
	CHECKCYCLE = 5
	
	report = open("report.csv","a")
	uFile = open("out.txt","r")
	
	if os.path.exists("prog.txt"):
		prog = int(open("prog.txt","r").readline())
		
	if prog != 0:
		for i in range(0, prog):
			uFile.readline()
	
	for uToCheck in uFile:
		check_url(uToCheck)
		
		prog += 1
	
		sleep(randint(0,3)) #Take it easy on requests
		if (prog  % CHECKCYCLE == 0):
			pfile = open("prog.txt","w")
			pfile.write(str(prog))
			pfile.close()
