import os
import requests
import shutil
import pandas as pd
import warnings
import logging

logging.basicConfig(level=logging.DEBUG)  # Add basic logging configuration

warnings.filterwarnings("ignore", category=DeprecationWarning)

# Function to read data from CSV file
def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df

# Function to format data for Discord and count passed/failed test cases
def format_discord_message(df, platform):
    formatted_data = ""

    # Extract the module name from the 'id' column
    df['module'] = df['id'].str.extract(r'(vplus/test/.+?/)')

    # Group the DataFrame by the 'module' column
    grouped_df = df.groupby('module')

    # Iterate over groups (modules)
    for module, group_df in grouped_df:
        total_tests = len(group_df)
        passed_count = group_df['status'].eq('passed').sum()
        failed_count = group_df['status'].eq('failed').sum()
        error_count = group_df['status'].eq('error').sum()

        # Get failed and error test cases
        failed_tests = group_df.loc[group_df['status'] == 'failed', ['id', 'message']]
        error_tests = group_df.loc[group_df['status'] == 'error', ['id', 'message']]

        # Generate the summary message for the module
        formatted_data += f"\n**===================== {platform.upper()} =====================**\n"
        formatted_data += f"Test Case Summary: ` {module} `\n"  # Bold borders for the test suite
        formatted_data += f"Total: {total_tests},\n"
        formatted_data += f"Passed: {passed_count},\n"
        formatted_data += f"Failed: {failed_count},\n"
        formatted_data += f"Error: {error_count}\n"

        if failed_count > 0:
            formatted_data += "\nList of Failed Test Cases:\n"
            for index, row in failed_tests.iterrows():
                if "assert False" in row['message']:
                    truncated_message = "assert False"
                else:
                    truncated_message = (row['message'][:45] + '...') if len(row['message']) > 45 else row['message']
                formatted_data += f"- [FAILED] {row['id']}\n"
                formatted_data += f"_message: {truncated_message}_\n"  # Italic for messages

        if error_count > 0:
            formatted_data += "\nList of Error Test Cases:\n"
            for index, row in error_tests.iterrows():
                if "assert False" in row['message']:
                    truncated_message = "assert False"
                else:
                    truncated_message = (row['message'][:45] + '...') if len(row['message']) > 45 else row['message']
                formatted_data += f"- [ERROR] {row['id']}\n"
                formatted_data += f"_message: {truncated_message}_\n"  # Italic for messages
                
        if error_count > 0 or failed_count > 0:
            formatted_data += "CC : <@402021347296804875> <@1077483182942863470> <@1020169083003600976> <@1072363842761408663>"        
        formatted_data += "\n"

    return formatted_data

# File path to your CSV file
# Mac Mini
# csv_file_path = '/Users/visionplus/Automation/AutomationWebSelenium/vplus/report/report.csv'  # Change this to the actual path
# My Local
csv_file_path = '/Users/ade/Documents/Automation/AutomationWebSelenium/vplus/report/report.csv'  # Change this to the actual path

# Read data from CSV file
df = read_csv(csv_file_path)

# Parse PLATFORM value from environment variable or use default "Unknown"
platform = os.getenv('PLATFORM', 'Unknown')

# Format data for Discord
formatted_data = format_discord_message(df, platform)

# Discord webhook setup
# Discord Private
# webhook_url = 'https://discord.com/api/webhooks/1211947885659430912/2MJhfYavdeWCJKeQQhGL48C31IswE_SI6uIkWqy74wohed_7w408h0E1sAPyrHuYeZd9'  # Replace with your actual webhook URL
# Mac Mini 
webhook_url = 'https://discord.com/api/webhooks/1164098964287660102/paNJevQJjaCy9oC-aY9Xy28L8L8WJgXFNa4tYr0eoJ7_nI3Qj4UwAdUBsk5PKD4icKXH'  # Replace with your actual webhook URL

# Folder path for the report
# Mac Mini
# report_folder = '/Users/visionplus/Automation/AutomationWebSelenium/vplus/report/'
# My Local
report_folder = '/Users/ade/Documents/Automation/AutomationWebSelenium/vplus/report/'

# Zip the report folder
shutil.make_archive(os.path.join(report_folder, 'report'), 'zip', report_folder)

# Path to the zip file
zip_file_path = os.path.join(report_folder, 'report.zip')

# Split the formatted message into chunks of maximum 2000 characters
chunk_size = 2000
chunks = [formatted_data[i:i+chunk_size] for i in range(0, len(formatted_data), chunk_size)]

# Send each chunk of the formatted message to Discord
for i, chunk in enumerate(chunks):
    if i == len(chunks) - 1:
        # Last chunk, send attachment file along with the chunk
        with open(zip_file_path, 'rb') as zip_file:
            files = {'file': ('report.zip', zip_file)}
            payload = {'content': chunk}
            
            # Make a POST request to the Discord webhook URL
            response = requests.post(webhook_url, data=payload, files=files)

            # Check the response status
            if response.status_code == 204:
                print("Last chunk and file sent successfully")
            else:
                print(f"Failed to send last chunk and file. Status code: {response.status_code}, Response content: {response.text}")
    else:
        # Not the last chunk, send only the chunk
        payload = {'content': chunk}
        
        # Make a POST request to the Discord webhook URL
        response = requests.post(webhook_url, data=payload)

        # Check the response status
        if response.status_code == 204:
            print("Chunk sent successfully")
        else:
            print(f"Failed to send chunk. Status code: {response.status_code}, Response content: {response.text}")

# Clean up: Remove the zip file
os.remove(zip_file_path)
