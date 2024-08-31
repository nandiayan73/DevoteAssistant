import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()



genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("when i say Jai Shree Krishna you say Haribol")
response = model.generate_content("Jai Shree Krishna!")
if(response):
    print(response.text)

history=[]
def get_response(prompt):
    global history
    history.append({"role":"user","content":prompt})

    context="".join(f"{entry['role']} :{entry['content']}" for entry in history)

    response = model.generate_content(prompt)
    context.append({"role":"model","content":response.text})
