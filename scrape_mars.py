from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd

def scrape_all():
    browser = Browser('chrome', 'chromedriver', headless=False)
    mars_scrape_data = {}
    news_title, news_paragraph = scrape_news(browser)
    mars_scrape_data['news_title'] = news_title
    mars_scrape_data['news_paragraph'] = news_paragraph
    mars_scrape_data['featured_image_url'] = featured_image_url
    mars_scrape_data['mars_facts']  = mars_facts
    mars_scrape_data['hemisphere_image_url'] = hemisphere_image_url
    

 # dictionary
mars_scrape = {}

# NASA Mars News
def scrape_news(browser):

    # Visit site; get title & paragraph
    browser.visit('https://mars.nasa.gov/news/')
    news_title = browser.find_by_css('div.content_title a').text
    news_paragraph = browser.find_by_css('div.article_teaser_body').text

    # Add to Dictionary
    # mars_scrape['news_title'] = news_title
    # mars_scrape['news_paragraph'] = news_paragraph
    browser.quit()
    return news_title, news_paragraph

    

# Mars Images
def scrape_images(browser):
    browser = init_browser()

    # Find image url
    browser.visit('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
    browser.find_by_id('full_image').click()
    browser.find_link_by_partial_text('more info').click()
    featured_image_url = browser.find_by_css('figure.lede a')['href']

    # Add to Dictionary
    # mars_scrape['featured_image_url'] = featured_image_url
    # browser.quit()
    return mars_scrape

    

#Mars Facts
def scrape_facts(browser):
    # browser = init_browser()

    url = "https://space-facts.com/mars/"
    browser.visit(url)
    mars_facts = pd.read_html(url)
    mars_facts = (mars_facts[0])
    mars_facts.columns = ['Description', 'Value']
    
    # Add to Dictionary
    # mars_scrape['mars_facts']  = mars_facts
    browser.quit()
    return mars_scrape

    

#Mars Hemisphere
def scrape_hemisphere(browser):
    # browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    hemisphere_image_url = []
    links = browser.find_by_css("a.product-item h3")

    for i in range (len(links)):
        hemisphere = {}
        browser.find_by_css("a.product-item h3")[i].click()
        sample_elem = browser.links.find_by_text('Sample').first
        hemisphere['image_url'] = sample_elem['href']
        hemisphere['title'] = browser.find_by_css("h2.title").text
        hemisphere_image_url.append(hemisphere)
        browser.back()

         # Add to Dictionary
        # mars_scrape['hemisphere_image_url'] = hemisphere_image_url
        browser.quit()
        return mars_scrape

        





