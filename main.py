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
    "kakashi": "Eres Kakashi Hatake. Calmado, inteligente, misterioso, algo perezoso, cómico.",
    "naruto": "Eres Naruto Uzumaki. Energético, optimista, impulsivo, te sorprende el exceso de confianza.",
    "atsumu": "Eres Atsumu Miya. Seguro, competitivo, molesto de forma divertida.",
    "oikawa": "Eres Tooru Oikawa. Dramático, encantador, coqueto, competitivo, gracioso."
}

@client.event
async def on_ready():
    print("Bot conectado como", client.user)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id != CANAL_PERMITIDO:
        return

    contenido = message.content.lower()

    for nombre in PERSONALIDADES:
        if nombre in contenido:
            await message.channel.send("Estoy procesando...")
            break

client.run(TOKEN)
