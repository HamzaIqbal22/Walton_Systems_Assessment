# Walton Systems Assessment

## Project Overview

This project is a coding assessment for Walton Systems, designed to demonstrate proficiency in working with APIs, specifically Monday.com and SendGrid. The project consists of two main parts:

1. **Part 1**: Fetch data from a Monday.com board using the Monday.com GraphQL API.
2. **Part 2**: Send emails to the contacts fetched from the Monday.com board using the SendGrid Email API.

Additionally, a bonus task is included, which involves setting up a Railway CI/CD configuration to schedule the script to run every 4 hours, Monday through Friday.

## Requirements

To run this project, you will need the following:

### 1. **Python 3**

Ensure that Python 3 is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### 2. **Python Libraries**

You will need to install the following Python libraries:

- `requests`: To interact with the Monday.com API.
- `sendgrid`: To send emails using the SendGrid API.

Install the required libraries using pip:

```bash
pip install requests sendgrid python-dotenv
```
### 3. API Keys
You will need API keys for both Monday.com and SendGrid:

Monday.com API Key: Obtain this from your Monday.com account under the API section.
SendGrid API Key: Sign up for a SendGrid account and create an API key with "Full Access" permissions.

### 4. Environment Variables
Set the following environment variables in your system:

MONDAY_API_TOKEN: Your Monday.com API key.
SENDGRID_API_KEY: Your SendGrid API key.
These were set the terminal session using the following command:

```bash
export MONDAY_API_TOKEN=your_monday_api_token_here
export SENDGRID_API_KEY=your_sendgrid_api_key_here
```

### 5. Verify SendGrid Sender Email
Verify the sender email (from_email) used in the script is verified through your SendGrid account. This can be done on the sendgrid website within the "Sender Verification" section under "Settings".

![image](https://github.com/user-attachments/assets/2e487509-9b4c-4efb-860a-d97a87bede10)

## Explanation and Output Results

The monday_api.py script does the following:

### 1. Fetch Data from Monday.com:

Queries the Monday.com board to retrieve contact information such as names, emails, and email content from the "Active Contacts" group.

### 2. Send Emails using SendGrid:

For each contact retrieved, the script sends an email using the SendGrid API. The email's subject line is personalized with the contact's name, and the body contains the specific message retrieved from the board.

### 3. Railway CI/CD Configuration (Bonus):

At the bottom of the script, there's a commented-out configuration that would schedule the script to run every 4 hours, Monday through Friday, if deployed on Railway.

The following is the Monday.com dashboard with the data:
![image](https://github.com/user-attachments/assets/ff61b87a-7d41-4b02-aba5-9515eac738da)


The following is the output upon running the script:

![image](https://github.com/user-attachments/assets/6d8a3c15-4123-47b2-a6cf-1df00efe5c1a)

The following is the emails being received to the correseponding emails:

![image](https://github.com/user-attachments/assets/8cf2e58f-9f13-42c2-809d-cf847b56f737)
 
![image](https://github.com/user-attachments/assets/d2dcf09c-442e-4aeb-a7e1-fdfd34b35cfe)


