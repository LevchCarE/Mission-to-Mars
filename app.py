from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping 

app = Flask(_name_)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#route for the html page
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()

#route for scrape data
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update({},mars_data,upsert=True)
    return redirect('/',code = 302)

#run flask
if __name__ == "__main__":
   app.run()