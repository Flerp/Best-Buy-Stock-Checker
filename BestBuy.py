import requests, webbrowser, datetime, os, playsound
from bs4 import BeautifulSoup
from playsound import playsound


def pull_html_data(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    return page.content


def check_stock_str(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    inventory_divs = soup.findAll("div", {"class": "fulfillment-add-to-cart-button"})
    return inventory_divs

now = datetime.datetime.now()
url = "enter_bestbuy_url"
page_html = pull_html_data(url)
stock_out_str = "c-button-disabled"
stock_in_str = "c-button-primary"
stock_output_string = str(check_stock_str(page_html))

if stock_out_str in stock_output_string:
    print(now)
    print("Out of stock")
    print(" ")
else:
    if stock_in_str in stock_output_string:
        webbrowser.open_new(url)
        print(now)
        print("In Stock!")
        print(" ")
        playsound('ALERT.mp3')
    else:
        print("Banned")
