
# III Link Checker
1. Takes a text file looking like `bib_id,url`
2.  Parses out empties and checks urls using [urllib2](https://docs.python.org/2/library/urllib2.html) 
3. Result in csv file `HTML_Status_Code,bib_id,url`

Has prelim whitelist feature