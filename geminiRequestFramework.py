import os 
import google.generativeai as genai
import time

from dotenv import load_dotenv, dotenv_values

load_dotenv() 
print(os.environ["API_KEY"])

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

start = time.time()
myfile = genai.upload_file("sampleAudio.mp3")
print(f"{myfile=}\n______________\nUploaded in {time.time() - start:.2f} seconds")

start = time.time()
response = model.generate_content([myfile, "Respond to this scam as a grandma would."])
print(f"{response.text}\n______________\nExecuted in {time.time() - start:.2f} seconds")