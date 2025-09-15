import requests
from dotenv import load_dotenv, dotenv_values

#Create a new API key programmatically from provisioning key
def create_key() -> str:
    load_dotenv()
    config = dotenv_values(".env")

    url = "https://openrouter.ai/api/v1/keys"

    payload = { "name": "string" }
    headers = {
        "Authorization": f'Bearer {config["PROVISIONING_API_KEY"]}',
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers) #Responds with new api key

    return response.json()['key'] 

print(create_key()) 