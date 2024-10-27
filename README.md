# NewHacks
StandardScaler and IsolationForest ML algorithms power the anomalous detection model, while Google's Gemini and ElevenLabs's TTS APIs power the live response component of Scam-Mah. The backend is handled by Python and integrated with an HTML/CSS/JS frontend. 

Dependencies/Libraries Used:
- google_generativeai
- python-dotenv
- playsound

The following API keys are needed and should be stored as "API_KEY" and "TTS_API_KEY" constants respectively within an .env file::
- Google Gemini (https://aistudio.google.com/app/apikey)
- ElevenLabs TTS (https://elevenlabs.io/app/speech-synthesis/text-to-speech)
