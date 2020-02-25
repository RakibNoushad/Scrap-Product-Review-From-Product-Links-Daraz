import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

#genarate a soup object by BeautifulSoup
def get_page(url):
    response = requests.get(url)

    if not response.ok:
        print('Server responded:', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')
    return soup

#from soup object find script tag with a specific type
def get_detail_data(soup):
    try:
        title = soup.find('script', {'type': 'application/ld+json'})

    except:
        title = ''

    try:
        pass
    except:
        pass

    f = open("review.csv", "a", encoding='utf-8')

    json_obj = json.loads(title.text)

    #Read Data from Daraz webpage. To understand these lines please go to Daraz.com.bd site and open background code.
    #You need a little knowledge about json Data format
    review_access = json_obj['review']
    for review_data in review_access:
        try:
            review_body = review_data['reviewBody']
        except:
            review_body = ''

        review_body = review_body.replace('\n', ' ')
        review_body = review_body.replace('\t', ' ')

        review_ratting = review_data['reviewRating']
        try:
            rating_value = review_ratting['ratingValue']
        except:
            rating_value = ''

        #append to csv file new Review Data
        f.write(review_body+","+rating_value+"\n")






def main():
    #creating a csv file for save Review Data
    f = open("review.csv", "w+", encoding='utf-8')
    headers = "Review Body, Rating Value"
    f.write(headers + "\n")

    #read text file containing Daraz category page link
    with open('link.txt', 'r') as g:
        for line in g:
            try:
                url = g.readline()
                get_detail_data(get_page(url))
                time.sleep(3)
            except:
                print("Problem in url")






if __name__ == '__main__':
    main()