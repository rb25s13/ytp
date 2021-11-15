from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    ytp_dict = {}

    # get the latest news title and blurb
    homeurl = './playlist.html'
    browser.visit(homeurl)

    html = browser.html
    soup = bs(html, 'html.parser')

    ytp_dict['title']  = soup.find('yt-formatted-string', class_='title').text
    ytp_dict['url'] = soup.find('a', class_='yt-formatted-string')['href']
    # ytp_dict['artist'] = soup.find('div', class_='article_teaser_body').text


    # Close the browser after scraping
    browser.quit()

    return ytp_dict