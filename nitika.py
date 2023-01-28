# parser
import time
from bs4 import BeautifulSoup
from selenium import webdriver


url = f'https://www.talent.com/jobs?l=Chicago%2C+Illinois&p=1&context=serp_pagination&id=2a3963a71b10'
browser = webdriver.Chrome()
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

print(soup)
    
    
