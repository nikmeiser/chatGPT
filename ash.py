
import os
import openai

# apply the API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# input text
text_prompt = str(input('Tell me what you want: '))
#text_prompt = (
#        "How to find the count of each word in a file using standard bash utilities on Linux or UNIX."
#        )
text_prompt = text_prompt.strip()

response = openai.Completion.create(
        engine="davinci-codex",
        prompt= text_prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.2,
        )

print(response.choices[0].text.strip())
