from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import requests


def scrape_info():
    # Set up Splinter
    # executable_path = {'executable_path': ChromeDriverManager().install()}
    # browser = Browser('chrome', **executable_path, headless=False)

    # ytp_dict = {}

    # # get the latest news title and blurb
    # homeurl = 'https://raw.githubusercontent.com/rb25s13/ytp/main/playlist.html'
    # browser.visit(homeurl)

    # html = browser.html
    # soup = bs(html, 'html.parser')




    # ytp_dict['title']  = soup.select("yt-formatted-string.title [title]")
    # ytp_dict['url'] = soup.find('a', class_='yt-simple-endpoint')['href']
    # div_url = soup.find_all('a', class_='yt-simple-endpoint style-scope yt-formatted-string')
    # ytp_dict['title'] = div_url.find('a')['href']
    # ytp_dict['url'] = soup.select("yt-formatted-string.title [href]")
    # if ytp_dict['url']:
    #     return ytp_dict['url'][0]
    # ytp_dict['artist'] = soup.find('div', class_='article_teaser_body').text


    # r = requests.get('https://raw.githubusercontent.com/rb25s13/ytp/main/playlist.html')
    # page = r.text
    # soup=bs(page,'html.parser')
    # res=soup.find_all('yt-formatted-string',{'class':'title'})
    # for l in res:
    #     print l.get("href")

    sourceCode = requests.get(url).text
    soup = BeautifulSoup(sourceCode, 'html.parser')
    domain = 'https://www.youtube.com'
    for link in soup.find_all("a", {'class':'title'}):
        href = link.get('href')
        if href.startswith('/watch?'):
            print(link.string.strip())
            print(domain + href + '\n')


    # Close the browser after scraping
    # browser.quit()

    return ytp_dict