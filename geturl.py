import urllib2
import sys

def main(url, filename):
    req = urllib2.Request(url)
    html = urllib2.urlopen(req).read()
    print html
    myFile = open(filename, 'wb')
    myFile.write(html)
    myFile.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('geturl.py   url  localfilename')
        sys.exit(-1)
    url = sys.argv[1]
    filename=sys.argv[2]    
    main(url,filename)