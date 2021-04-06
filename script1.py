#!/usr/bin/python3.5

from bs4 import BeautifulSoup
from urllib.request import urlopen

site = 'https://chico.craigslist.org/d/apts-housing-for-rent/search/apa'
html = urlopen(site)
file = open("pid.txt", "w")
counter1 = 0
counter2 = 0

soup = BeautifulSoup(html, 'lxml')
total = soup.find('span', class_='totalcount')
for listing in soup.find_all('p'):
#  counter1 += 1
#  if counter1 == 1500:
#    print(listing.time.text)
#  print(counter1)

  #for listing in soup.find_all('span', class_='result-price'):
  if (listing.find('span', class_='result-price') != None) & (listing.find('span', class_='result-hood') != None):
    i = listing.find('span', class_='result-price')
    counter2 += 1
    print(counter2,"value of i = ",i)
    file.write(str(i) + "\n") 
    j = listing.find('time', class_='result-date')
    k = listing.find('span', class_='result-hood')
    print("DATE:",j.text)
    print("CITY:",k.text)
    #price = listing.text[2:6]
    #print(price)
    #price = int(price)
    #if price <=250 and price > 100:
    #    print(listing.text)
    link_end = listing.a['href']
    #url = urljoin(BASE, link_end)
    print("url = ", link_end)
    #print("\n")file.write(str(i) + "\n")
    print(total.text)

#x=`diff top5 next | grep -c <`
#if [$x -gt 0]
#then
#  echo "changed"
#fi
