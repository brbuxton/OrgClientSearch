import requests
import os


def search_meraki_clients(api_key, organization_id, mac_address):
    url = f"https://api.meraki.com/api/v1/organizations/{organization_id}/clients/search"
    headers = {
        'X-Cisco-Meraki-API-Key': api_key,
        'Content-Type': 'application/json'
    }
    params = {
        'mac': mac_address
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def main():
    api_key = os.getenv('MERAKI_DASHBOARD_API_KEY')
    organization_id = 'YOUR_ORGANIZATION_ID'  # Replace YOUR_ORGANIZATION_ID with your ID

    mac_address = input("Please enter the client MAC address: ")

    client_info = search_meraki_clients(api_key, organization_id, mac_address)

    if client_info:
        print("Client found:", client_info)
    else:
        print("Client not found or an error occurred.")


if __name__ == "__main__":
    main()
