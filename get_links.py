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
            href = href.replace("&list=LM", "")
            playlist.append(domain + href)
            print(domain + href + '\n')
    df = pd.DataFrame(playlist,columns=['link'])
    df.to_csv('./resources/playlist.csv', index=False)

getPlaylistLinks('https://raw.githubusercontent.com/rb25s13/ytp/main/resources/playlist.html')
