import requests
import pandas as pd
import shutil
import os

# Function to read data from CSV file
def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df

# Function to format data for Discord and count passed/failed test cases
def format_discord_message(df):
        # Extract the module name from the 'id' column
    df['module'] = df['id'].str.extract(r'(test/.+?/)')

    # Group the DataFrame by the 'module' column
    grouped_df = df.groupby('module')

    # Initialize variables to store information
    formatted_data = ""

    # Iterate over groups (modules)
    for module, group_df in grouped_df:
        total_tests = len(group_df)
        passed_count = group_df['status'].eq('passed').sum()
        failed_count = group_df['status'].eq('failed').sum()

        # Get unique modules for failed tests
        failed_modules = group_df.loc[group_df['status'] == 'failed', 'id'].unique()

        # Generate the summary message for the module
        formatted_data += "=========================================================\n"
        formatted_data += f"**Test Case Summary: {module} **\n"
        formatted_data += f"Total: {total_tests},\n"
        formatted_data += f"Passed: {passed_count},\n"
        formatted_data += f"Failed: {failed_count}\n"

        if failed_count > 0:
            formatted_data += "\n ** List of Failed Test Cases: **\n"
            for failed_module in failed_modules:
                formatted_data += f"- [FAILED] {failed_module}\n"

        
        formatted_data += "\n All Test Case are Successfully Executed \n"
        
        formatted_data += "\n"

    return formatted_data

# Function to split a message into chunks
def split_message(message, chunk_size=2000):
    return [message[i:i+chunk_size] for i in range(0, len(message), chunk_size)]

# File path to your CSV file
csv_file_path = '/Users/ade/Documents/Automation/AutomationWebSelenium/report/report.csv'  # Change this to the actual path

# Read data from CSV file
df = read_csv(csv_file_path)

# Get the unique value from the 'id' column for naming the zip file
zip_name = df['id'].iloc[0]  # You can adjust this depending on how you want to extract the name

# Format data for Discord
formatted_data = format_discord_message(df)

# Split the message into chunks if it exceeds 2000 characters
message_chunks = split_message(formatted_data)

# Discord webhook setup
webhook_url = 'https://discord.com/api/webhooks/1211947885659430912/2MJhfYavdeWCJKeQQhGL48C31IswE_SI6uIkWqy74wohed_7w408h0E1sAPyrHuYeZd9'

# Folder path for the report
report_folder = '/Users/ade/Documents/Automation/AutomationWebSelenium/report/'

# Print the formatted data to the console
print(formatted_data)

# Zip the report folder
shutil.make_archive(os.path.join(report_folder, zip_name), 'zip', report_folder)

# Path to the zip file
zip_file_path = os.path.join(report_folder, f'{zip_name}.zip')

# Send the zip file to Discord
with open(zip_file_path, 'rb') as zip_file:
    files = {'file': ('report.zip', zip_file)}
    response = requests.post(webhook_url, files=files)

# Print more information about the Discord API response
print(f"Discord API response: {response.status_code}, {response.text}")

# Check the response status
if response.status_code == 200:
    print(f"Zip file '{zip_name}.zip' sent successfully")
else:
    print(f"Failed to send zip file. Status code: {response.status_code}, Response content: {response.text}")

# Clean up: Remove the zip file
os.remove(zip_file_path)
