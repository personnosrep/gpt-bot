import requests
import json
import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# Set the token.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Define whatever this is.
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".",intents=intents)


@bot.tree.command(name="define",description="Get a definition from the urban dictionary")
async def slash_command(interaction:discord.Interaction, word: str):


    response = requests.get(f"http://api.urbandictionary.com/v0/define?term={word}")
    data = response.text

    if word == 'arya' or word == 'Arya':
        await interaction.response.send_message('Short goblin')

#C:/Users/Amin/Desktop/coding stuffs/python/urban bot
        
    else:
        if response.status_code == 200:

            try:


                parse_data = json.loads(data)

                firstdef = parse_data["list"][1]

                author = (firstdef["author"].replace('[', '')).replace(']', '')

                definition = (firstdef["definition"].replace('[', '')).replace(']', '')

                word = (firstdef["word"].replace('[', '')).replace(']', '')


                await interaction.response.send_message(f'\nauthor: {author}\nword: {word}\ndefinition: {definition}\n')

            
            except:
                await interaction.response.send_message('word does not exist')

            



        else:
            await interaction.response.send_message(f'Error. Code {response.status_code}')
    







@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.tree.sync()








bot.run(DISCORD_TOKEN)


    


