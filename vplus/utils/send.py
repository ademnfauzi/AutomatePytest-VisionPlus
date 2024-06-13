import discord
from discord.ext import commands
import requests
from requests.auth import HTTPBasicAuth

# Replace with your own credentials
DISCORD_TOKEN = 'MTI0OTY0OTYxNzI4MTQ4Mjg3Mw.GEmoZ2.McrpJLZqH_w00r7_3a4g-G_NnCpiOqD_J9NMsM'
JENKINS_URL = 'http://10.9.18.207:8080/job/WebSelenium/'

# Jenkins credentials
JENKINS_USER = 'visionplus'
JENKINS_API_TOKEN = 'your_api_token_here'

# Create a bot instance with command prefix '/'
intents = discord.Intents.default()
intents.message_content = True  # Enable the Message Content intent if needed

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def run(ctx):
    # Trigger Jenkins job with basic authentication
    auth = HTTPBasicAuth(JENKINS_USER)
    response = requests.post(JENKINS_URL, auth=auth, verify=True)  # Disable SSL verification
    if response.status_code == 201:
        await ctx.send('Jenkins job triggered successfully!')
    else:
        await ctx.send(f'Failed to trigger Jenkins job. Status code: {response.status_code}')

bot.run(DISCORD_TOKEN)
