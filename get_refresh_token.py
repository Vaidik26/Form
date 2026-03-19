import os
import requests
from dotenv import load_dotenv

load_dotenv()

ZOHO_CLIENT_ID = os.getenv("ZOHO_CLIENT_ID")
ZOHO_CLIENT_SECRET = os.getenv("ZOHO_CLIENT_SECRET")
REDIRECT_URI = "https://www.zoho.com"

def generate_refresh_token(grant_token):
    print("Exchanging Grant Token for a Refresh Token...")
    url = "https://accounts.zoho.in/oauth/v2/token"
    payload = {
        "grant_type": "authorization_code",
        "client_id": ZOHO_CLIENT_ID,
        "client_secret": ZOHO_CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": grant_token
    }
    
    response = requests.post(url, data=payload)
    data = response.json()
    
    if "refresh_token" in data:
        print(f"\n✅ SUCCESS! Your Refresh Token is:\n{data['refresh_token']}\n")
        print("Please copy this refresh token and update your .env file as ZOHO_REFRESH_TOKEN !!")
    else:
        print("\n❌ ERROR generating refresh token:")
        print(data)

if __name__ == "__main__":
    print("Welcome! Let's generate your Zoho Refresh Token.")
    grant_token = input("\nPlease paste the 'code' parameter you got from the authorization URL:\n> ")
    generate_refresh_token(grant_token.strip())
