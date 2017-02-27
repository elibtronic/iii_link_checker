#Preps input files

import re

o = open("out.txt","w")

with open("856_dump.txt") as f:
	
	#Header
	f.readline()
	
	for line in f:
		url_part = line.split(",")
		if url_part[1] == '""\r\n':
			continue
		else:
			#print url_part[1]
			for u in re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F])|(?:[;]))+',url_part[1]):
				if re.search('http[s]?://dr.library.brocku.ca',u)\
				or re.search('http[s]?://www.library.brocku.ca/gifts',u)\
				or re.search('http[s]?://hdl.handle.net/10464',u)\
				or re.search('http[s]?://catalogue.library.brocku.ca',u)\
				or re.search('http[s]?://sfx.scholarsportal.info',u):
					pass
				else:
					cu = re.sub('http\:\/\/proxy\.library\.brocku\.ca/login\?url\=','',u)
					o.write(url_part[0].strip('" ')+" , "+cu.strip(' ')+'\n')
					
