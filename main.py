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

    if message.channel.id != CANAL_PERMITIDO:
        return

    contenido = message.content.lower()

    for nombre in PERSONALIDADES:
        if nombre in contenido:
            try:
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}"
    }

    api_url = "https://router.huggingface.co/hf-inference/models/mistralai/Mistral-7B-Instruct-v0.2"

    prompt = PERSONALIDADES[nombre] + "\nUsuario: " + message.content

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 200
        }
    }

    response = requests.post(api_url, headers=headers, json=payload)

    print("STATUS:", response.status_code)
    print("TEXT:", response.text)

    if response.status_code != 200:
        await message.channel.send("Error con la IA. Revisa logs.")
        return

    try:
        resultado = response.json()
    except:
        print("No es JSON válido")
        return

    if isinstance(resultado, list):
        reply = resultado[0].get("generated_text", "No hubo respuesta.")
        await message.channel.send(reply)
    else:
        print("Respuesta inesperada:", resultado)

except Exception as e:
    print("ERROR CRÍTICO:", e)

            break

client.run(TOKEN)
