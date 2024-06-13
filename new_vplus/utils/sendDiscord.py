import requests
import pandas as pd

# Function to read data from CSV file
def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df

# Function to format data for Discord
def format_discord_message(df):
    formatted_data = ""
    for index, row in df.iterrows():
        name = row['name']
        status = row['status']
        message = row['message']

        formatted_data += f"**|Test Case:** {name}\n**|Status:** {status}\n**|Message:** {message}\n\n"

    return formatted_data

# Function to split a message into chunks
def split_message(message, chunk_size=2000):
    return [message[i:i+chunk_size] for i in range(0, len(message), chunk_size)]


# File path to your CSV file
csv_file_path = '/Users/visionplus/Automation/AutomationWebSelenium/report/report.csv'  # Change this to the actual path

# Read data from CSV file
df = read_csv(csv_file_path)

# Filter necessary columns
filtered_df = df[['name', 'status', 'message']]

# Format data for Discord
formatted_data = format_discord_message(filtered_df)

# Split the message into chunks if it exceeds 2000 characters
message_chunks = split_message(formatted_data)


# Discord webhook setup
webhook_url = 'https://discord.com/api/webhooks/1211947885659430912/2MJhfYavdeWCJKeQQhGL48C31IswE_SI6uIkWqy74wohed_7w408h0E1sAPyrHuYeZd9'

# Send each message chunk separately
for chunk in message_chunks:
    # Create a payload with the message
    payload = {
        'content': chunk,
    }

    # Make a POST request to the Discord webhook URL
    response = requests.post(webhook_url, json=payload)

    # Check the response status
    if response.status_code == 204:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Status code: {response.status_code}, Response content: {response.text}")