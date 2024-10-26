import os 
import google.generativeai as genai
import time
from dotenv import load_dotenv, dotenv_values

class geminiRequestFramework: 
    
    model = None
    myfile = None

    def uploadAudio(self):
        start = time.time()
        geminiRequestFramework.myfile = genai.upload_file("sampleAudio.mp3")
        print(f"{geminiRequestFramework.myfile=}\n______________\nUploaded in {time.time() - start:.2f} seconds")

    def generateResponse(self):
        start = time.time()
        response = geminiRequestFramework.model.generate_content([geminiRequestFramework.myfile, "Respond to this scam as a grandma would."])
        print(f"{response.text}\n______________\nExecuted in {time.time() - start:.2f} seconds")
        return response.text
    
    def __init__(self):
        load_dotenv() 
        print(os.environ["API_KEY"])
        genai.configure(api_key=os.environ["API_KEY"])
        geminiRequestFramework.model = genai.GenerativeModel("gemini-1.5-flash")