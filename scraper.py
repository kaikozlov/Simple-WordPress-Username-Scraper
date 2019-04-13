# import libraries
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv

#specify WordPress URL
quote_page = ""

#establish author number variable
author = 2

while True:
    author = author+1
    #query the website and return the html to the variable "page"
    page = urlopen(Request(quote_page + str(author), headers={'User-Agent': 'Mozilla/5.0'}))
	

    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
    name_box = soup.find('meta', attrs={'name':'description'})
    print(name_box)
    print(quote_page + str(author))

    # open a csv file with append, so old data will not be erased
    with open('index.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        
        writer.writerow([name_box, quote_page + str(author)])
