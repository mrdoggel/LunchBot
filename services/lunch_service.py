import datetime
from scraper.lunch_scraper import parseEtsLunches, parseF4yLunches, parseFlowLunches

def getAll():
    lunches = {}
    etsLunches = parseEtsLunches()
    f4yLunches = parseF4yLunches()
    flowLunches = parseFlowLunches()
    lunches.update(etsLunches)
    lunches.update(f4yLunches)
    lunches.update(flowLunches)
    return lunches

def getDaily():
    day = datetime.date.today().strftime("%A")
    lunches = getAll()
    if (day == "Tuesday"):
        ets_today = {'ets':{'english':lunches.get('ets').get('english').get("Thuesday")}}
        f4y_today = {'f4y':{'english':lunches.get('f4y').get('english').get("Thuesday")}}
    else:
        ets_today = {'ets':{'english':lunches.get('ets').get('english').get(day)}}
        f4y_today = {'f4y':{'english':lunches.get('f4y').get('english').get(day)}}
    flow_today = {'flow':{'english':lunches.get('flow').get('english').get(day)}}
    lunches.update(ets_today)
    lunches.update(f4y_today)
    lunches.update(flow_today)
    return lunches