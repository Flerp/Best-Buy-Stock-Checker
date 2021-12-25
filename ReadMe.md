# Best Buy Stock Checker

If you enjoy my work and would like to send me a tip  

BTC: 3MuNv3vVygXkYBKkJk56sgaWqCdg1L2tBh  
ETH: 0x8bBDCD275addfc8fA084854c3123e72b015dAaE6  
DOGE: DGyouCkRvXZ7xoSSGTy8t1Yx5tNvuaVNk9

## Why did I make this?

Seeing all of the super sketchy browser addons, with terms of services that said they collected every possible bit of personal information made me unseasy, so I made this.
After a few days I was able to snag my 30 series GPU at MSRP.

## What does this do?

This is a simple script that will pull a webpage from Best Buy and check if an item is in stock.
This script does not purchase for you, and performs no automation for purchasing in any way.

There are two variants of this script

### Standard
If in stock: The script will play an incredibly loud alarm sound, print to the console, and open your default web browser to the product page so that you may buy it.  
If out of stock: The script will print out to the console with a timestamp.

### Text
If in stock: The script will send an email to your phone's MMS/SMS provider email (phonenumber@mmsdomain.com) with the URL so that you can purchase the item via your phone.  
If out of stock: The script will print out to the console with a timestamp.  

## How to setup

### Requirements

Python
Python Packages: requests, playsound, bs4

### Standard

1. Copy the ALERT.mp3 to the same directory as the script.
2. Open the BestBuy.py with your preferred text editor.
3. Navigate to like line 18 (url = "enter_bestbuy_url").
4. Replace enter_bestbuy_url with a url from Best Buy to watch.
5. Save.
6. Create a script to run the python script repeatedly (See example).

### Text

Note: If emailing from gmail you will need to create an app password

1. Open the BestBuy_text.py with your preferred text editor.
2. Navigate to like line 17 (url = "enter_bestbuy_url").
3. Replace enter_bestbuy_url with a url from Best Buy to watch.
4. Navigate to lines 25-29
5. Replace (enter_\*) with the requested information (email, password, phone number email, email server, email server port)
6. Save.
7. Create a script to run the python script repeatedly (See example).

## Example Script
```
@echo off
Title BestBuy
pip install requests playsound bs4
:repeat
powershell "py BestBuy.py | tee BestBuy.txt -append"
:numbergen
set /a num=%random% %%11 +5
echo Waiting %num% seconds
echo.
echo.
ping -n %num% 127.0.0.1 >nul
goto repeat
```

This is an example script for Windows operating systems.
It installs the required packages, then runs the python script, while outputting everything to a log file.  
It then generates a random number between 6 and 15, pings localhost for that amount of seconds, then repeats.  

There is a complete example in the example folder that is ready to use.
