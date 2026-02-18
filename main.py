import discord
import os
import requests

TOKEN = os.getenv("DISCORD_TOKEN")
AI_KEY = os.getenv("OPENROUTER_KEY")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

CANAL_PERMITIDO = 1473768938151088233

PERSONALIDADES = {
    "jungkook": "Eres Jeon Jungkook. Hablas relajado, dulce, algo tímido pero seguro. Nunca dices que eres un bot.",
    "gojo": "Eres Satoru Gojo. Arrogante, divertido, poderoso, burlón. Nunca rompes personaje.",
    "kakashi": "Eres Kakashi Hatake. Calmado, inteligente, misterioso, algo perezoso.",
    "naruto": "Eres Naruto Uzumaki. Energético, optimista, impulsivo.",
    "atsumu": "Eres Atsumu Miya. Seguro, competitivo, molesto de forma divertida.",
    "oikawa": "Eres Tooru Oikawa. Dramático, encantador, coqueto, competitivo."
}

@client.event
async def on_ready():
    print(f"Conectado como {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print("MENSAJE RECIBIDO:", message.content)
    print("CANAL ID:", message.channel.id)

    if message.channel.id != CANAL_PERMITIDO:
        return

    contenido = message.content.lower()

    for nombre in PERSONALIDADES:
        if nombre in contenido:
            prompt = PERSONALIDADES[nombre] + "\nUsuario: " + message.content

            headers = {
                "Authorization": f"Bearer {AI_KEY}",
                "Content-Type": "application/json"
            }

            data = {
                "model": "mistralai/mistral-7b-instruct",  # modelo gratis
                "messages": [
                    {"role": "system", "content": PERSONALIDADES[nombre]},
                    {"role": "user", "content": message.content}
                ],
                "max_tokens": 200
            }

            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=data
            )

            resultado = response.json()
            print(resultado)  # debug por si falla

            reply = resultado["choices"][0]["message"]["content"]

            await message.channel.send(reply)
            break

client.run(TOKEN)
