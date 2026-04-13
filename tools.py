import requests
import os
from datetime import datetime

# -------- Weather Tool --------
def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=%C+%t"
    r = requests.get(url, timeout=5)
    if r.status_code == 200:
        return f"Weather in {city}: {r.text}"
    return "Unable to fetch weather"

# -------- Math Tool --------
def calculate(expression: str):
    try:
        allowed = "0123456789+-*/(). "
        if not all(c in allowed for c in expression):
            return "Invalid math expression"
        return str(eval(expression))
    except Exception:
        return "Calculation error"

# -------- String Tool --------
def string_transformer(data: str):
    try:
        text, action = data.rsplit("|", 1)
        action = action.strip().lower()

        if action == "uppercase":
            return text.upper()
        if action == "lowercase":
            return text.lower()
        if action == "reverse":
            return text[::-1]
        if action == "word_count":
            return str(len(text.split()))
        return "Unsupported operation"
    except Exception:
        return "Format: text | action"

# -------- Time Tool --------
def get_time(_: str = ""):
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# -------- System Info Tool --------
def system_info(_: str = ""):
    return os.uname().sysname

AVAILABLE_TOOLS = {
    "get_weather": get_weather,
    "calculate": calculate,
    "string_transformer": string_transformer,
    "get_time": get_time,
    "system_info": system_info
}
