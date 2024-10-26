import os
import requests
from dotenv import load_dotenv, dotenv_values
from playsound import playsound

class ttsRequestFramework:
    
    api_key = None
    voice_id = None
    url = None
    stability = None
    similarityBoost = None
    
    def convertTTS(self, text):
        payload = {
            "text": text,
            "voice_settings": {
                "stability": 0.5,               # CNG to VAR
                "similarity_boost": 0.6         # CNG to VAR
            }
        }
        headers = {
            "xi-api-key": ttsRequestFramework.api_key,
            "Content-Type": "application/json"
        }

        response = requests.request("POST", ttsRequestFramework.url, json=payload, headers=headers)

        # Check for success
        if response.status_code == 200:
            # Save the audio file
            with open("static/audio/output.mp3", "wb") as file:
                file.write(response.content)
            playsound('static/audio/output.mp3')
            print("Audio generated successfully!")
            return True
        else:
            print("Error:", response.status_code)
            print(response.text)
            return False

    def __init__(self, stability, similarityBoost):
        load_dotenv() 
        ttsRequestFramework.api_key = os.environ["TTS_API_KEY"]
        ttsRequestFramework.voice_id = "78pDRD8cI8CahmrAekML"
        ttsRequestFramework.url = f"https://api.elevenlabs.io/v1/text-to-speech/{ttsRequestFramework.voice_id}"
        ttsRequestFramework.stability = stability
        ttsRequestFramework.similarityBoost = similarityBoost