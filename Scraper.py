from bs4 import BeautifulSoup as bs
import requests
import re
import csv

#open and format csv file
f = csv.writer(open('Videos.csv', 'w'))
f.writerow(['Number','Link'])

youtube_base = 'https://www.youtube.com/'

with open('Channels.csv', "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        r = requests.get(row['Link'])
        page = r.text
        soup = bs(page,'html.parser')

        res = soup.find_all('a',href=re.compile('/watch'))
        for a in res:
            vid=a.get('href')
            title=a.get('title')
            x=0

            link=('{0}{1}'.format(youtube_base, vid))
            if title is None:
                continue
            else:
                #print(title)
                print (link)
                f.writerow ([x,link])
                x += 1

