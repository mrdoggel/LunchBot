def section(text):
    return {
        "type": "section",
        "text": text
    }

def setHeader(text):
    return {
        "type": "header",
        "text": text
    }

def mrkdwn_text(text):
    return {
        "type":"mrkdwn",
        "text": text
    }

def plain_text(text):
    return {
        "type":"plain_text",
        "text": text,
        "emoji": True
    }

def list_text(items):
    finnished_text = ""
    for item in items:
        finnished_text += f"• {item}\n"
    return finnished_text

def format_data(items, title):
    title = section(mrkdwn_text(f"*{title}*"))
    if (items != None):
        formatted_data = section(mrkdwn_text(list_text(items)))
    else:
        formatted_data = section(mrkdwn_text("• No lunch options available today"))
    return [title, formatted_data]

def format_daily(data):
    header = [setHeader(plain_text("Lunch options for today"))]
    ets_data = data.get("ets").get("english")
    ets = format_data(ets_data, "Eat the street")
    f4y_data = data.get("f4y").get("english")
    f4y = format_data(f4y_data, "Fresh4You")
    flow_data = data.get("flow").get("english")
    flow = format_data(flow_data, "Flow")
    return header + ets + f4y + flow

def format_weekly(data):
    header = [setHeader(plain_text("Lunch options for this week"))]
    ets_data = extractLunchFromEveryDay(data.get("ets"))
    ets = format_data(ets_data, "Eat the street")
    f4y_data = extractLunchFromEveryDay(data.get("f4y"))
    f4y = format_data(f4y_data, "Fresh4You")
    flow_data = extractLunchFromEveryDay(data.get("flow"))
    flow = format_data(flow_data, "Flow")
    return header + ets + f4y + flow

def extractLunchFromEveryDay(data):
    monday = data.get("english").get("Monday")
    if (data.get("english").get("Thuesday") != None):
        tuesday = data.get("english").get("Thuesday")
    else:
        tuesday = data.get("english").get("Tuesday")
    wednesday = data.get("english").get("Wednesday")
    thursday = data.get("english").get("Thursday")
    friday = data.get("english").get("Friday")
    return monday+tuesday+wednesday+thursday+friday