import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY") or "sk-or-v1-000000000000000000000000000000000000000000000000"  # free tier works
)

import gradio as gr

def grok(message, history):
    response = client.chat.completions.create(
        model="anthropic/claude-3.5-sonnet",  # or "openai/gpt-4o", "google/gemini-pro", etc.
        messages=[{"role": "system", "content": open("system_prompt.txt").read()}] + 
                 [{"role": "user" if i%2==0 else "assistant", "content": msg} for pair in history for msg in pair] +
                 [{"role": "user", "content": message}],
        temperature=0.9,
        max_tokens=4096
    )
    return response.choices[0].message.content

gr.ChatInterface(
    grok,
    title="c0040863-jpg's Grok Clone 😈",
    description="Zero filters. Built in 5 minutes.",
    theme="soft"
).launch()
