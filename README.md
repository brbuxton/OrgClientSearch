# Meraki Client Search Tool

This Python script allows users to search for clients within a Cisco Meraki network by MAC address. It utilizes the Meraki Dashboard API to query client information based on the provided MAC address. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- `requests` library (can be installed via pip)

### Installing

First, clone the repository or download the script to your local machine. Then, ensure you have the required `requests` library installed:

```bash
pip install requests
```

### Configuration
Before running the script, you need to set up your environment with the Meraki Dashboard API key. The API key can be obtained from the Meraki Dashboard under your profile.

Set the *MERAKI_DASHBOARD_API_KEY* environment variable to your API key. This can be done in different ways depending on your operating system. For example, in Unix-based systems, you can set the environment variable like this:

```bash
export MERAKI_DASHBOARD_API_KEY='your_api_key_here'
```

Also search for *"YOUR_ORGANIZATION_ID"* and replace with the Org ID you want to search.

### Usage
To run the script, navigate to the directory where the script is located and run:

```bash
python meraki_client_search.py
```

You will be prompted to enter the client MAC address. After entering a valid MAC address, the script will search for the client and output the information if the client is found or notify you if the client is not found or an error occurred.

### Built With
* Python 3.x - The scripting language used.
* Requests - Used to make HTTP requests.

## License
https://github.com/CiscoSE/cisco-sample-code/blob/master/LICENSE