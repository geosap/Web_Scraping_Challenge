from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd

def scrape_all():
    mars_scrape_data = {}
    browser = Browser('chrome', 'chromedriver', headless=False)

    news_title, news_paragraph = scrape_news(browser)
    mars_scrape_data['news_title'] = news_title
    mars_scrape_data['news_paragraph'] = news_paragraph
    mars_scrape_data['featured_image_url'] = scrape_feature_image_url(browser)
    mars_scrape_data['mars_facts']  = scrape_mars_facts()
    mars_scrape_data['scrape_hemisphere'] = scrape_hemisphere(browser)
 # dictionary
    return mars_scrape_data
    
# NASA Mars News
def scrape_news(browser):
    # Visit site; get title & paragraph
    browser.visit('https://mars.nasa.gov/news/')
    news_title = browser.find_by_css('div.content_title a').text
    news_paragraph = browser.find_by_css('div.article_teaser_body').text

    return news_title, news_paragraph

    # Mars Images
def scrape_feature_image_url(browser):

    # Find image url
    browser.visit('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
    browser.find_by_id('full_image').click()
    browser.find_link_by_partial_text('more info').click()
    featured_image_url = browser.find_by_css('figure.lede a')['href']
    return featured_image_url

#Mars Facts
def scrape_mars_facts():
    url = "https://space-facts.com/mars/"
    mars_facts = pd.read_html(url)[0]
    mars_facts.columns = ['Description', 'Value']
    mars_facts = mars_facts.to_html(classes = 'table table-stripped mars')

    return mars_facts
  
#Mars Hemisphere
def scrape_hemisphere(browser):
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    hemisphere_image_url = []
    links = browser.find_by_css("a.product-item h3")

    for i in range(len(links)):
        hemisphere = {}
        browser.find_by_css("a.product-item h3")[i].click()
        sample_elem = browser.links.find_by_text('Sample').first
        hemisphere['image_url'] = sample_elem['href']
        hemisphere['title'] = browser.find_by_css("h2.title").text
        hemisphere_image_url.append(hemisphere)
        browser.back()

    browser.quit()
    return hemisphere_image_url

        





