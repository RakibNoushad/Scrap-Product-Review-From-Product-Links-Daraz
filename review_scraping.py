import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time




def get_page(url):
    response = requests.get(url)


    if not response.ok:
        print('Server responded:', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')
    return soup

def get_detail_data(soup):
    try:
        title = soup.find('script', {'type': 'application/ld+json'})
            #.join(str(soup.find('script')).split("\n"))
    except:
        title = ''

    try:
        pass
    except:
        pass

    f = open("review.csv", "a", encoding='utf-8')


    json_obj = json.loads(title.text)

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



        f.write(review_body+","+rating_value+"\n")






def main():
    f = open("review.csv", "w+", encoding='utf-8')
    headers = "Review Body, Rating Value"
    f.write(headers + "\n")

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