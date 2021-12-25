import requests, datetime, os, smtplib
from bs4 import BeautifulSoup


def pull_html_data(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    return page.content


def check_stock_str(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    inventory_divs = soup.findAll("div", {"class": "fulfillment-add-to-cart-button"})
    return inventory_divs

now = datetime.datetime.now()
url = "enter_best_buy_url"
page_html = pull_html_data(url)
stock_out_str = "c-button-disabled"
stock_in_str = "c-button-primary"
stock_output_string = str(check_stock_str(page_html))


#FILL THESE IN /start
sendemailaddress = "enter_email_address"
emailpass = "enter_email_password"
receiveemailaddress = ['enter_phone_number@enter_phone_mms_domain.com']
emailserver = "enter_email_server_here"
emailport = "enter_email_port_here"
#FILL THESE IN /end

mailsubject = "Product Available"


mailbody = url
smtpvar1 = smtplib.SMTP_SSL(emailserver, emailport)
mailmessage = """\
From: %s
To: %s
Subject: %s

%s
""" % (sendemailaddress, ", ".join(receiveemailaddress), mailsubject, mailbody)


#print(stock_output_string)
#print(check_stock_str(page_html))

if stock_out_str in stock_output_string:
    print(now)
    print("Out of stock")
    print(" ")
else:
    if stock_in_str in stock_output_string:
        print(now)
        print("In Stock!")
        print(" ")
        smtpvar1.set_debuglevel(1)
        smtpvar1.ehlo()
        smtpvar1.login(sendemailaddress, emailpass)
        smtpvar1.sendmail(sendemailaddress, receiveemailaddress, mailmessage)
        smtpvar1.close()
    else:
        print("Temp Banned Probably")
