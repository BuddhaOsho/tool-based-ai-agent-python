from dotenv import load_dotenv
from openai import OpenAI
import json
import os

from prompts import SYSTEM_PROMPT
from tools import AVAILABLE_TOOLS
from schemas import AgentResponse
from intents import detect_intent

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def main():
    history = [{"role": "system", "content": SYSTEM_PROMPT}]

    print("Advanced AI Agent CLI\n")

    while True:
        user_input = input("User ➜ ")
        intent = detect_intent(user_input)

        history.append({
            "role": "user",
            "content": f"[intent={intent}] {user_input}"
        })

        while True:
            response = client.chat.completions.parse(
                model="gemini-2.5-flash",
                response_format=AgentResponse,
                messages=history
            )

            parsed = response.choices[0].message.parsed
            history.append({"role": "assistant", "content": json.dumps(parsed.model_dump())})

            if parsed.step == "PLAN":
                print("PLAN ➜", parsed.content)
                continue

            if parsed.step == "TOOL":
                tool_fn = AVAILABLE_TOOLS.get(parsed.tool)
                tool_result = tool_fn(parsed.input) if tool_fn else "Tool not found"

                history.append({
                    "role": "developer",
                    "content": json.dumps({
                        "step": "OBSERVE",
                        "tool": parsed.tool,
                        "input": parsed.input,
                        "output": tool_result
                    })
                })
                continue

            if parsed.step == "OUTPUT":
                print("OUTPUT ➜", parsed.content, "\n")
                break

if __name__ == "__main__":
    main()
