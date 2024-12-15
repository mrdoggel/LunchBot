import re
import os
from string import digits
from curl.curl import get
from bs4 import BeautifulSoup

url = "https://widget.inisign.com/Widget/Customers/Customer.aspx"

def getAllLunches(html):
    soup = BeautifulSoup(html, 'html.parser')
    norwegian_rows = soup.findAll('div', attrs={'class':'row', 'class':'left-item'})
    english_rows = soup.findAll('div', attrs={'class':'row', 'class':'right-item'})
    formatted_norwegian_rows = {'norwegian':formatLunchRows(norwegian_rows)}
    formatted_english_rows = {'english':formatLunchRows(english_rows)}
    formatted_norwegian_rows.update(formatted_english_rows)
    return formatted_norwegian_rows

def formatLunchRows(rows):
    formatted_rows = {}
    for row in rows:
        day = row.h1.text
        parsed_items = []
        items = row.findAll('div', attrs={'class':'menu-container'})
        for item in items:
            bottom_item = findBottomMenuContainerRecursively(item)
            if (bottom_item != None):
                parsed_items.append(bottom_item.text.translate(str.maketrans('', '', digits)).replace(u'\xa0', u' ').replace(u',', u' ').strip())
        formatted_rows.update({day:parsed_items})
    return formatted_rows

def findBottomMenuContainerRecursively(item):
    children = item.findAll('div', attrs={'class':'menu-container'})
    if (not children):
        return item
    for child in children:
        findBottomMenuContainerRecursively(child)

def parseEtsLunches():
    ets = get(url, {'token':'6e5cc038-e918-4f97-9a59-d2afa0456abf'})
    etsLunches = {'ets':getAllLunches(ets)}
    return etsLunches

def parseF4yLunches():
    f4y = get(url, {'token':'a8923cdb-9d92-46bc-b6a4-d026c2cf9a89'})
    f4yLunches = {'f4y':getAllLunches(f4y)}
    return f4yLunches

def parseFlowLunches():
    flow = get(url, {'token':'756a5aa2-a95f-4d15-ad5a-59829741075b'})
    flowLunches = {'flow':getAllLunches(flow)}
    return flowLunches



