import sys
import urllib2, httplib, re, urllib, os

def fetch(id):
    # URL
    url = "http://www.leboncoin.fr/emploi/"+str(id)+".htm"
    
    # REQUETE

    result = urllib2.Request(url)
    
    try:
        f = urllib2.urlopen(result)
    except urllib2.HTTPError, err:
        return

    data = f.read()

    # REGEX - EMAIL
    reg = "[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]{2,5}"
    comReg = re.compile(reg)
    result = comReg.findall( data.decode('utf-8', 'ignore') )
    # PRINT RESULT
    for find in result :
        f = open('emails.txt', 'a+')
        f.write(find)
        f.write('\n')
        for line in f:
            print 'lo'
        f.close

        f = open('number.txt', 'w+')
        f.write(str(id))
        for line in f:
            print 'lo'
        f.close
    #fin for
#fin fetch

# id from where you start
id = 706596642

# id to go
i  = 706293442

while i > 0 :
    fetch(i)
    i = i-1
#fin while
