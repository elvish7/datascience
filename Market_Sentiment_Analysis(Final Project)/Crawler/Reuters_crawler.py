
import pandas as pd
import datetime as dt
import numpy as np
import requests
import time
from bs4 import BeautifulSoup
import pandas_datareader.data as web
import re

# grab links to news articles from reuter's archive page
# ten+ articles are displayed on each page
url_links = []

sections = ['technology', 'markets', 'business','fundfunds', 'gc07', 'exchange-traded-funds']
for i in range(1,3277):
    for section in sections:
        try:
            url = 'https://www.reuters.com/news/archive/' + section + 'news?view=page&page=' + str(i) + '&pageSize=10'
    #         print(url)
            html = requests.get(url)
            content = html.content
            content.decode().strip().replace('\t','').split('\n')
            soup = BeautifulSoup(content, "html.parser")
            for tags in soup.find_all('a'):
                if re.search('article', tags['href']):
                    url_links.append(tags['href'])
            print(i, end = ' ')
        except:
            print(section)
            continue
            # some linkes may be duplicated thus we only select those that only appear once
final_urls = []
for url in url_links:
    if url not in final_urls:
        final_urls.append(url)
print('Articles Count:', len(final_urls))

# retreive the title, publish time and content for each article

title_all = []
time_all = []
content_all = []
url_all = []

count = 0
for url in final_urls:
    try:
        link = 'https://www.reuters.com' + url
        page = requests.get(link).content
        soup = BeautifulSoup(page, "html.parser")
        newsTitle = soup.title.text.lstrip()
        print(count, end = ' ')
        newsTime = soup.find_all("div", {"class": 'ArticleHeader_date'})[0].text
        newsContent = ''
        for tag in soup.find_all('p'):
            newsContent += tag.text

        title_all.append(newsTitle)
        time_all.append(newsTime)
        content_all.append(newsContent)
        url_all.append(link)
        file = pd.DataFrame({'Title' : title_all, 'Time':time_all, 'Content':content_all, 'Link':url_all})
        file['Date'] = [x.split('/')[0] for x in file['Time'].tolist()]
        file['Date'] = pd.to_datetime(file['Date'])
        file.sort_values(['Date'], inplace = True)

        file['Len'] = [len(x) for x in file['Content']]
        file = file[file['Len'] >= 600]

        file.to_csv('Articles2.csv')
        count += 1
    except:
        continue

# remove spaces infront of titles
# title_all = [x.lstrip() for x in title_all]
