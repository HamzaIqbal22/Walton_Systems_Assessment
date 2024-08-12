# Walton Systems Assessment

## Project Overview

This project is a coding assessment for Walton Systems, designed to demonstrate proficiency in working with APIs, specifically Monday.com and SendGrid. The project consists of two main parts:

1. **Part 1**: Fetch data from a Monday.com board using the Monday.com GraphQL API.
2. **Part 2**: Send emails to the contacts fetched from the Monday.com board using the SendGrid Email API.

Additionally, a bonus task is included, which involves setting up a Railway CI/CD configuration to schedule the script to run every 4 hours, Monday through Friday.

## Requirements

To run this project, you will need the following:

### 1. **Python 3.x**

Ensure that Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### 2. **Python Libraries**

You will need to install the following Python libraries:

- `requests`: To interact with the Monday.com API.
- `sendgrid`: To send emails using the SendGrid API.
- `python-dotenv` (optional): To manage environment variables through a `.env` file.

Install the required libraries using pip:

```bash
pip install requests sendgrid python-dotenv
