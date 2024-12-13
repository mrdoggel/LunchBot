from bs4 import BeautifulSoup
import re
from string import digits

def parseDinner(html):
    return getAllDinneres(html)

def getAllDinneres(html):
    dinners = [];
    soup = BeautifulSoup(html, 'html.parser')
    norwegian_rows = soup.findAll('div', attrs={'class':'row', 'class':'left-item'})
    english_rows = soup.findAll('div', attrs={'class':'row', 'class':'right-item'})
    formatted_norwegian_rows = {'norwegian':formatRows(norwegian_rows)}
    formatted_english_rows = {'english':formatRows(english_rows)}
    formatted_norwegian_rows.update(formatted_english_rows)
    return formatted_norwegian_rows

def formatRows(rows):
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

