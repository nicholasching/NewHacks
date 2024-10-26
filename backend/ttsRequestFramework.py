import os
import requests
from dotenv import load_dotenv, dotenv_values
from playsound import playsound
load_dotenv() 

# Replace with your actual API key
api_key = os.environ["TTS_API_KEY"]

# Select the voice (replace with your desired voice ID)
voice_id = "78pDRD8cI8CahmrAekML"

url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

payload = {
    "text": "Oh my, a data breach? Now that sounds scary. I don't know anything about computers, but my grandson, he's a whiz with them! I'll give him a call and see what he says.",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.6
    }
}
headers = {
    "xi-api-key": api_key,
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

# Check for success
if response.status_code == 200:
    # Save the audio file
    with open("output.mp3", "wb") as file:
        file.write(response.content)
    playsound('output.mp3')
    print("Audio generated successfully!")
else:
    print("Error:", response.status_code)
    print(response.text)