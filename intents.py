def detect_intent(query: str) -> str:
    query = query.lower()

    if any(word in query for word in ["weather", "temperature", "rain"]):
        return "weather"

    if any(word in query for word in ["add", "subtract", "multiply", "divide", "+", "-", "*", "/"]):
        return "math"

    if any(word in query for word in ["uppercase", "lowercase", "reverse", "word count"]):
        return "string"

    if any(word in query for word in ["time", "date", "today", "now"]):
        return "time"

    if any(word in query for word in ["summarize", "summary"]):
        return "summarization"

    return "general"
