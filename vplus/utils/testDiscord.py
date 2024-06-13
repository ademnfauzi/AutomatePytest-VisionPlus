import discord
from requests import post

# It's recommended to store the token securely (not directly in the code)
discord_token = "MTI0OTY0OTYxNzI4MTQ4Mjg3Mw.GEmoZ2.McrpJLZqH_w00r7_3a4g-G_NnCpiOqD_J9NMsM"  # Replace with your actual token

# Replace with your Jenkins server details
jenkins_url = "http://10.9.18.207:8080/job/WebSelenium/"

# Define the intents your bot needs (replace with specific intents if needed)
intents = discord.Intents.default()  # Use default intents for now

# Create the Discord client with intents
client = discord.Client(intents=intents)

# Command prefix (change as desired)
command_prefix = "/"


@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(command_prefix + "jenkins"):
        try:  # Add try-except block for error handling
            job_name = message.content.split()[1]  # Extract job name after command
        except IndexError:
            await message.channel.send(f"Please provide a job name after the command (e.g., '!jenkins WebSelenium').")
            return

        # No authentication headers needed

        # Send POST request to Jenkins Webhook URL
        response = post(jenkins_url + "/buildWithParameters")

        if response.status_code == 201:
            await message.channel.send(f"Job '{job_name}' triggered successfully!")
        else:
            await message.channel.send(f"Error triggering job: {response.text}")


client.run(discord_token)
