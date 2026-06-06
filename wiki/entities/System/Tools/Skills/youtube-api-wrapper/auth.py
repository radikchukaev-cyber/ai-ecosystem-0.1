"""
YouTube API Wrapper - Authentication Module
Handles OAuth 2.0 flow for YouTube Data API v3. 
Caches credentials to minimize user prompts and handles token refresh automatically.
"""

import os
import pickle
import logging
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Scopes required for the application
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
CREDENTIALS_FILE = 'client_secret.json'
TOKEN_FILE = 'token.pickle'

def get_authenticated_service():
    """
    Validates existing credentials or prompts the user to log in.
    Returns an authenticated YouTube service object.
    """
    creds = None
    
    # Try to load existing credentials
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
            
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
                logging.info("Credentials refreshed successfully.")
            except Exception as e:
                logging.error(f"Failed to refresh credentials: {e}")
                creds = None
                
        if not creds:
            if not os.path.exists(CREDENTIALS_FILE):
                raise FileNotFoundError(f"Missing {CREDENTIALS_FILE}")
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
            
        # Save the credentials for the next run
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    return build('youtube', 'v3', credentials=creds)

if __name__ == "__main__":
    # Test authentication
    try:
        service = get_authenticated_service()
        print("Successfully authenticated with YouTube API.")
    except Exception as e:
        print(f"Authentication failed: {e}")
