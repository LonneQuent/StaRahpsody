import cohere
import tiktoken
import openai
import os
from openai import OpenAI
import pandas as pd

def generateur_poeme(input_1,input_2,input_3):
    client = OpenAI(api_key='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')

    #On utilise l'API de ChatGPT comme générateur de poème en lui donnant les instructions sélectionnées précédemment.
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "tu es "+input_1+" de l'univers de "+input_3+""},
            {"role": "user","content": "fais moi un poème de type "+input_2+" en te comportant comme "+input_1},
        ],
        model="gpt-3.5-turbo",
    )

    return chat_completion.choices[0].message.content
