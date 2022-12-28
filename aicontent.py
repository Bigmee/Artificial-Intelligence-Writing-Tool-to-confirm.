import os
import openai
import config
openai.api_key = config.OPENAI_API_KEY

def openAIQuery (query):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= query, 
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    
    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response["choices"][0]["text"]
        else:
            answer = "Oops sorry, you beat DaVinci this time"
    else:
        answer = "Oops sorry you beat DaVinci this time"
    
    return answer