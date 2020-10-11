# import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import os

# Create flask app
app = Flask(__name__)

# Setup mongo connection locally
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db" )


# Create route to index.html & grabs docs from mongo
@app.route('/')
def index_root():

    # find data
    mars_scrape = mongo.db.mars_scrape.find_one()
    return render_template("index.html", mars_scrape = mars_scrape)


# Route triggering scrape 
@app.route("/scrape")
def scrape():
    
    # Run scraped functions
    mars_scrape = mongo.db.mars_scrape
    mars_news = scrape_mars.scrape_news()
    feature_images = scrape_mars.scrape_images()
    mars_facts = scrape_mars.scrape_facts()
    mars_hemi_images = scrape_mars.scrape_hemisphere()
    print(mars_facts)
    mars_scrape.update({}, mars_facts,upsert=True)

    return redirect("/", code=302)

if __name__ == '__main__':
    app.run(debug=True)