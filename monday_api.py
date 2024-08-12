import os
import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Set up API tokens and board ID
monday_api_token = os.getenv("MONDAY_API_TOKEN")
sendgrid_api_key = os.getenv("SENDGRID_API_KEY")

board_id = "7209817422"

# Set up the headers for the Monday.com API request
headers = {
    "Authorization": monday_api_token,
    "Content-Type": "application/json"
}

# Define the GraphQL query to fetch items from the "Active Contacts" group
query = """
{
  boards(ids: [%s]) {
    groups(ids: "topics") {
      title
      items_page {
        items {
          name
          column_values {
            id
            text
          }
        }
      }
    }
  }
}
""" % board_id

# Make the request to the Monday.com API
response = requests.post("https://api.monday.com/v2", json={'query': query}, headers=headers)
print("Raw response:", response.text)

contacts = []

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    if 'data' in data:
        groups = data['data']['boards'][0]['groups']
        for group in groups:
            if group['title'] == 'Active Contacts':
                for item in group['items_page']['items']:
                    contact_name = item['name']
                    email = None
                    email_content = None
                    for column_value in item['column_values']:
                        if column_value['id'] == 'contact_email':  
                            email = column_value['text']
                        elif column_value['id'] == 'long_text4':  
                            email_content = column_value['text']
                    if email and email_content:
                        contacts.append({
                            "name": contact_name,
                            "email": email,
                            "content": email_content
                        })

        # Print out the fetched contact data
        for contact in contacts:
            print(f"Contact: {contact['name']}\nEmail: {contact['email']}\nEmail Content: {contact['content']}\n")
            print(sendgrid_api_key)

    else:
        print("Unexpected response structure, 'data' key not found.")
else:
    print(f"Failed to fetch data: {response.status_code}")
    print(response.text)

# Function to send an email using SendGrid
def send_email(to_email, subject, content):
    message = Mail(
        from_email='hamza.iqbal@torontomu.ca',  # Replace with your email
        to_emails=to_email,
        subject=subject,
        plain_text_content=content)
    
    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        print(f"Email sent to {to_email}, Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")

# Send emails to the contacts using SendGrid
for contact in contacts:
    send_email(contact["email"], f"Hello {contact['name']}", contact["content"])

# **Bonus Section**
# Railway config to run the script every 4 hours, Monday to Friday
# [scripts.scheduler]
# command = "python monday_api.py"
# schedule = "0 */4 * * 1-5"