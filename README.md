
# III Link Checker

1. Takes a text file looking like `bib_id,url`
2.  Parses out empties and checks urls using [urllib2](https://docs.python.org/2/library/urllib2.html) 
3. Result in csv file `HTML_Status_Code,bib_id,url`

Following errors are tracked: HTML Status Codes, 404,200,etc and Timeouts
Grep pattern based whitelist available

`prep.py` - will extract out URLS and bibs from input file, one per line, and does the whitelisting

`check_urls.py` - takes output of previous and does actual checking and logging.

