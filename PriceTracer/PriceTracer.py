from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(executable_path=r"/Users/domi/Proggen/GitHub/HTMLforNoobs/PriceTracer/chromedriver")

wunschpreis = 115

while True:

    browser.get("https://www.amazon.de/Amazon-Kindle-Paperwhite-Wasserfest-Doppeltem-Speicherplatz/dp/B07747FR44/ref=sr_1_1?__mk_de_DE=ÅMÅŽÕÑ&dchild=1&keywords=kindle&qid=1614375594&sr=8-1")

    aktpreis = browser.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text
    aktpreis = aktpreis.replace(',', '.')
    aktpreis = aktpreis.split(' ')
    aktpreis = float(aktpreis[0])

    if wunschpreis >= aktpreis:
        print("Jetzt kaufen!")
        break
    time.sleep(60*60)

