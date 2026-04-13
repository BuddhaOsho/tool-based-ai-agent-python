from dotenv import load_dotenv
from openai import OpenAI
import json
import os

from prompts import SYSTEM_PROMPT
from tools import AVAILABLE_TOOLS
from schemas import AgentResponse

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def main():
    message_history = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    print("AI Agent CLI started. Type your query.\n")

    while True:
        user_query = input("User ➜ ")
        message_history.append({"role": "user", "content": user_query})

        while True:
            response = client.chat.completions.parse(
                model="gemini-2.5-flash",
                response_format=AgentResponse,
                messages=message_history
            )

            parsed = response.choices[0].message.parsed
            message_history.append(
                {"role": "assistant", "content": json.dumps(parsed.model_dump())}
            )

            if parsed.step == "PLAN":
                print("PLAN ➜", parsed.content)
                continue

            if parsed.step == "TOOL":
                tool_name = parsed.tool
                tool_input = parsed.input

                print(f"TOOL ➜ {tool_name}({tool_input})")

                tool_output = AVAILABLE_TOOLS[tool_name](tool_input)

                message_history.append({
                    "role": "developer",
                    "content": json.dumps({
                        "step": "OBSERVE",
                        "tool": tool_name,
                        "input": tool_input,
                        "output": tool_output
                    })
                })
                continue

            if parsed.step == "OUTPUT":
                print("\nOUTPUT ➜", parsed.content, "\n")
                break

if __name__ == "__main__":
    main()
