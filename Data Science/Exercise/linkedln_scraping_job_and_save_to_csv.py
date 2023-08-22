# -*- coding: utf-8 -*-
"""Linkedln Scraping job and Save to CSV.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1auqX9dx41iMj0FC12zy9idvVEoZ-gjoy

Sulaiman Alfarsi
Linkedln Scraping job and Save to CSV
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

from IPython.core.display import display_javascript
def extract(page):
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

  url =f'https://www.linkedin.com/jobs/search?keywords=Python%20Developer&location=Oman&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0{page}'
  r = requests.get(url, headers)
  soup = BeautifulSoup(r.content, 'html.parser')
  return soup


def trasnform(soup):
  divs = soup.find_all('div',class_="base-search-card__info")
  for item in divs:
    title =item.find('h3').text.strip()
    company = item.find('h4').text.strip()
    location = item.find('span').text.strip()
    time = item.find('time').text.strip()

    job ={
        'title': title,
        'company': company,
        'location':location,
        'time':time

    }

    joblist.append(job)

  return




joblist= []

for i in range(0,40,10):
  print(f'Getting page',{i})
  c = extract(0)
  trasnform(c)

df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')