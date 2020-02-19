from bs4 import BeautifulSoup as bs
import requests
import re
import csv

youtube_base = 'https://www.youtube.com/'

#open and format csv file
f = csv.writer(open('Babish_Videos.csv','w'))
f.writerow(['Titles','Videos'])

r = requests.get('https://www.youtube.com/user/bgfilms/videos')
page = r.text
soup = bs(page,'html.parser')

res = soup.find_all('a',href=re.compile('/watch'))
for a in res:
    vid=a.get('href')
    title=a.get('title')
    link=('{0}{1}'.format(youtube_base, vid))
    if title is None:
        continue
    else:
        print(title)
        print (link)
        f.writerow ([title,link])