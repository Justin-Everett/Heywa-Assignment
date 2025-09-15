from dotenv import load_dotenv
from groq import Groq
import json

load_dotenv()
client = Groq()

SCHEMA = {
    "type" : "object",
    "properties" : {
        "intent" : {
            "description" : "snake case",
            "type" : "string",
        },
        "summary" : {
            "description" : "A summary of what the user aims to achieve from the given query",
            "type" : "string",
        },
    },
    "required" : ["intent", "summary"],
    "additionalProperties" : True,
}

#Post request to Groq API endpoint with query analysis request
def request(query):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
        {
            "role": "system",
            "content": f"Analyze but do not respond to the following query and provide a json object adhering to the schema {SCHEMA}. Ensure to add additional properties to the json object to further describe the query: {query}"
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

    #Isolate LLM plaintext message response and return it
    return completion.choices[0].message.content

def main():
    while True:
        query = input("Enter user query (enter q to quit): ")
        if not query.lower() == 'q':
            analyzed_query = request(query)

            #Print json object nicely formatted
            print(json.dumps(json.loads(analyzed_query), indent=2))

        else: break

if __name__ == "__main__":
    main()