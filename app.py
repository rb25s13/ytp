# from flask import Flask, render_template, redirect
# from flask_pymongo import PyMongo
# import scrape_ytp

# from bs4 import BeautifulSoup as bs
# import requests

# r = requests.get('https://raw.githubusercontent.com/rb25s13/ytp/main/playlist.html')
# page = r.text
# soup=bs(page,'html.parser')
# res=soup.find_all('yt-formatted-string',{'class':'title'})
# for l in res:
#     print l.get("href")




from bs4 import BeautifulSoup
import requests

def getPlaylistLinks(url):
    sourceCode = requests.get(url).text
    soup = BeautifulSoup(sourceCode, 'html.parser')
    domain = 'https://www.youtube.com'
    for link in soup.find_all("a", {'class':'yt-simple-endpoint'}):
        href = link.get('href')
        if href.startswith('/watch?'):
            print(link.string.strip())
            print(domain + href + '\n')

getPlaylistLinks('https://raw.githubusercontent.com/rb25s13/ytp/main/playlist.html')

# # Create an instance of Flask
# app = Flask(__name__)

# # Use PyMongo to establish Mongo connection
# mongo = PyMongo(app, uri="mongodb://localhost:27017/ytp")


# # Route to render index.html template using data from Mongo
# @app.route("/")
# def home():

#     # Find one record of data from the mongo database
#     ytp = mongo.db.collection.find_one()

#     # Return template and data
#     return render_template("index.html", tube=ytp)


# # Route that will trigger the scrape function
# @app.route("/scrape")
# def scrape():

#     # Run the scrape function
#     ytp_data = scrape_ytp.scrape_info()

#     # Update the Mongo database using update and upsert=True
#     mongo.db.collection.update({}, ytp_data, upsert=True)

#     # Redirect back to home page
#     return redirect("/")


# if __name__ == "__main__":
#     app.run(debug=True)
