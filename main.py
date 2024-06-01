from gpt4all import GPT4All
import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# get stuff.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
API_KEY = os.getenv("API_KEY")
model = GPT4All("nous-hermes-llama2-13b.Q4_0.gguf")

# Define whatever this is.
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".",intents=intents)


@bot.tree.command(name="prompt",description="Get a response idk")
async def slash_command(interaction:discord.Interaction, prompt: str):

            await interaction.response.defer()
            model = GPT4All("nous-hermes-llama2-13b.Q4_0.gguf")

            output = model.generate(str(prompt))
            print(output)
            await interaction.followup.send(output)
        
    

@bot.tree.command(name="help",description="HELP ME")
async def slash_command(interaction:discord.Interaction):

    await interaction.response.send_message('**Reasons for dead bot(that ive discovered so far)**:\n- Gemini gets mad when u say no-no words\n- too long of a message\n- Asking how to make methamphetamine')






@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.tree.sync()








bot.run(DISCORD_TOKEN)
