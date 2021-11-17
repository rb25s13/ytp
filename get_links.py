from bs4 import BeautifulSoup
import requests
import pandas as pd

def getPlaylistLinks(url):
    sourceCode = requests.get(url).text
    soup = BeautifulSoup(sourceCode, 'html.parser')
    domain = 'https://www.youtube.com/'
    # list_dict = {}
    playlist = []
    for link in soup.find_all("a", {'class':'yt-simple-endpoint style-scope yt-formatted-string'}):
        href = link.get('href')
        if href.startswith('watch?'):
            playlist.append(domain + href)
            print(domain + href + '\n')
    df = pd.DataFrame(playlist)
    df.to_csv('playlist.csv', index=False)

getPlaylistLinks('https://raw.githubusercontent.com/rb25s13/ytp/main/playlist.html')
