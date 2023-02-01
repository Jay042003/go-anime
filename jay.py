from selenium import webdriver
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.keys import Keys
from selenium .webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import lxml, requests, time


path = 'C:\\webdrivers\\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get('https://animepahe.com/play/66f426f7-9e20-8646-b0f4-9fd4c61bbb14/c7f535bb5115e1492e63b821c994238b5d6043a9a6b5445cc5d2e317514d3a6a')
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0",
}

# webpage = requests.get("https://animepahe.com/play/66f426f7-9e20-8646-b0f4-9fd4c61bbb14/c7f535bb5115e1492e63b821c994238b5d6043a9a6b5445cc5d2e317514d3a6a",headers=headers).text
soup = BeautifulSoup(driver.page_source,'lxml')
risk =driver.get(soup.find_all('a',class_='dropdown-item')[-1]['href'])
time.sleep(6)
soup2 = BeautifulSoup(driver.page_source,'lxml')
driver.get(soup2.find('a',class_='btn btn-primary btn-block redirect')['href'])

time.sleep(10)