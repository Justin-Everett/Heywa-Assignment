from dotenv import load_dotenv
from groq import Groq

load_dotenv()

query = "What is the meaning of life"

#Boilerplate Groq post request from their docs
client = Groq()
completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
    {
        "role": "user",
        #Set up prompt to be able to handle a varied user input
        "content": f"Provide a json object answering the following question: {query}" 
    }
    ],
    temperature=1,
    max_completion_tokens=8192,
    top_p=1,
    reasoning_effort="medium",
    stream=False,
    response_format={"type": "json_object"},
    stop=None
)

print(completion.choices[0].message.content)