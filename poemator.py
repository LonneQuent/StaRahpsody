## Générateur de poèmes basé sur les sagas
import openai
from openai import OpenAI

client = OpenAI(api_key='votre_clé_API')

choix_film_user = None
perso_user = None
choix_poem_user = None

#On utilise l'API de ChatGPT comme générateur de poème en lui donnant les instructions sélectionnées précédemment.
chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "tu es "+perso_user+" de l'univers de "+choix_film_user},
        {"role": "user","content": "fais moi un poème de type "+choix_poem_user+" en te comportant comme "+perso_user},
    ],
    model="gpt-3.5-turbo",
)

#On affiche le poème.
print("\n Voici votre poème:\n")
print(chat_completion.choices[0].message.content)