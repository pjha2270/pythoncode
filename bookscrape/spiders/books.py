import scrapy
from pathlib import Path
from pymongo import MongoClient
import datetime

client = MongoClient("mongodb+srv://prakash-123:Meronepal1@scrapy-mongo.qctvs5f.mongodb.net/")
db = client.scrapy
def insertToDb(page, title, rating,thumbnail, price, inStock ):
    collection = db[page]
    doc = {"title": title, "rating": rating, "thumbnail":thumbnail, "price": price, "inStock": inStock, "date":datetime.datetime.now()}
    inserted = collection.inserted_one(doc)
    return inserted.inserted_id
    
class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://toscrape.com"]
    def start_requests(self):
        urls = [
            "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"books-{page}.html"
        bookdetail = {}
        
        # Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
        cards = response.css(".product_pod")
        for card in cards:
            title = cards.css("h3>a::text").get()
            print(title)
            
            rating = card.css(".star-rating").attrib["class"].split(" ")[1]
            print(rating)
            
            thumbnail = card.css("thumbnail_container img")
            thumbnail =thumbnail.attrib["src"]
            print(thumbnail.attrib["src"])
            
            price = card.css(".price_color::text").get()
            print(price)
            
            inStock = card.css(".inStock")
            if len(inStock.css(".ocon-ok")) > 0:
                inStock = True
            else:
                inStock = False
            insertToDb(page, title, rating,thumbnail, price, inStock )