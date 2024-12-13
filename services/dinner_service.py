import os
import datetime
from scraper.scraper import parseDinner
from curl.curl import get

def parseEtsDinners(url):
    ets = get(url, {'token': os.environ['ets_token']})
    etsDinners = {'ets':parseDinner(ets)}
    return etsDinners

def parseF4yDinners(url):
    f4y = get(url, {'token': os.environ['f4y_token']})
    f4yDinners = {'f4y':parseDinner(f4y)}
    return f4yDinners

def parseFlowDinners(url):
    flow = get(url, {'token': os.environ['flow_token']})
    flowDinners = {'flow':parseDinner(flow)}
    return flowDinners

def parseAllDinners():
    url = "https://widget.inisign.com/Widget/Customers/Customer.aspx"
    dinners = {}
    etsDinners = parseEtsDinners(url)
    f4yDinners = parseF4yDinners(url)
    flowDinners = parseFlowDinners(url)
    dinners.update(etsDinners)
    dinners.update(f4yDinners)
    dinners.update(flowDinners)
    return dinners

def parseDailyDinners():
    day = datetime.date.today().strftime("%A")
    dinners = parseAllDinners()
    ets_today = dinners.get('ets').get('english').get(day)
    return ets_today