import os 
import google.generativeai as genai
import time

from dotenv import load_dotenv, dotenv_values

load_dotenv() 
print(os.environ["API_KEY"])

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

start = time.time()
response = model.generate_content("Return test if this is recieved.")
print(f"{response.text}\n______________\nExecuted in {time.time() - start:.2f} seconds")