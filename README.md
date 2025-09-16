# Heywa-Assignment

## Project Overview

Having chosen track 1, this project takes a plaintext user query and returns a JSON object dissecting the query.

## Setup Instructions

- Download /src folder (if in an editor clone repository via 'https://github.com/Justin-Everett/Heywa-Assignment.git')
- Navigate to /src directory
- Run `pip install -r requirements.txt` to install dependencies
- Run `python3 query.py` to execute the query analysis LLM task

## My Approach

- Given that the LLM task requires a json output with 2 mandatory fields per query, I drew on my past work with LLM API calls and decided that a schema is necessary to properly format the output. The challenge that I hadn't dealt with before was the adaptible nature of the json object outputs; depending on the query they needed different properties/fields. This issue was resolved pretty quickly, as the LLM API response was capable of adding additional fields according to the input query, which I was able to make conform closely to the expected output after changing the prompt a bit.
- I initially planned to work with openrouter.ai but could not find a free tier, so I abandoned this and used Groq instead which proved quick, free, and easy to work with.
- Important considerations:
  - Keep schema and prompt brief to reduce token input, therefore (if using a paid API) decreasing cost of each request, as well as decreasing the time taken per response.
  - Played around with the temperature and reasoning effort, but ended up sticking with original values based on quality of response and time per request.
  - A key design decision was, based on the input examples from the task, that the schema required newly generated properties per-request. It would likely provide higher quality results if a larger schema was used to explicitly provide several optional properties, but this would result in a much larger number of input tokens and would potentially not encompass required details for some prompts. Therefore, I decided to use a minimal schema and generate additional properties through the request prompt.
- How system could be improved over time:
  - Although my brief testing kept the temperature and reasoning effort the same, these and the other call parameters could be optimized over time as a result of some form of user feedback system, providing increasing output clarity over time.
  - Further tinkering could be applied to prompt and/or schema to reduce number of input tokens while achieving the same output.

## AI Tool Usage

- Although I did not use any AI tools to make this project, the structure of the call request and the schema were inspired by a previous project of mine in which I used ChatGPT to aid in learning these concepts. Therefore, this does have some transitive use of AI tools involved, but nothing directly.
- All the code was written and debugged entirely by myself.
