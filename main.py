from slack.chat import send
from services.lunch_service import getAll, getDaily
from services.lunch_format_service import format_daily, format_weekly

send(format_daily(getDaily()), "Lunch options for today", "#test")
send(format_weekly(getAll()), "Lunch options for this week", "#test")

