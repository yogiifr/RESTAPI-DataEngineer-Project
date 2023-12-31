# Youtube Data API

## Project Description
The Bookstoscrape Books Scraper is a Python web crawler built with the Scrapy framework to extract information about books from books.toscrape.com The crawler follows specific rules to navigate through the website and scrape details such as book title, price (£), and availability.

## Steps
1. **Obtain API :** 
```python
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
```
The script starts by importing necessary modules from the Scrapy framework. `CrawlSpider` is a specialized spider class in Scrapy for crawling websites, and `Rule` is used to define rules for crawling and parsing. `LinkExtractor` helps in extracting links from web pages.



## Video Reference
For a visual guide and additional insights, you can refer to the following video:

**Title:** Youtube API for Python: How to Create a Unique Data Portfolio Project

**Link:** [Watch Video](https://www.youtube.com/watch?v=D56_Cx36oGY&t=630s)
