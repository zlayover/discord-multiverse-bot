import discord
import os
import requests

TOKEN = os.getenv("DISCORD_TOKEN")
HF_TOKEN = os.getenv("HF_TOKEN")

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
            try:
                headers = {
                    "Authorization": f"Bearer {HF_TOKEN}"
                }

                api_url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

