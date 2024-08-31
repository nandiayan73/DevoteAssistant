import google.generativeai as genai
from dotenv import load_dotenv
import os
import subprocess
import json

load_dotenv()

def playMusic(chat_session):
    track_name=chat_session.send_message("Enter the track name of the song, only the song's track name and no other replies,just enter the track name and no other replies, if user dont mention the track name you can reply with any track name. Just reply with a track naem any other reply will lead to error")
    chat_session.send_message("Now you have to reply the name of the artist, if the user dont select artist you can anyone you like, but reply only the name of the artist and nothing")
    artist_name=chat_session.send_message("Enter the artist name of the song, only the song's artist name and no other replies")
    data={
        "track_name":track_name.text,
        "artist_name":artist_name.text,
    }
    print(data)
    dict_str = json.dumps(data)

    command = ['python3', 'playMusic.py', dict_str]

    result = subprocess.run(command, capture_output=True, text=True)
    return 1

def create_chat_session():
  """Creates a new chat session with themodel="gemini-3.5-turbo" Gemini API."""
  return genai.ChatSession(model = genai.GenerativeModel('gemini-1.5-flash'))  

def send_message(chat_session, message):
  """Sends a message to the chat session and returns the response."""
  response = chat_session.send_message(message)
  return response.text

def main():
  # Replace with your API key
  genai.configure(api_key=os.environ["API_KEY"])

  chat_session = create_chat_session()

  while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
      break

    # response = send_message(chat_session, user_input)
    playMusic(chat_session)
    # print("Gemini:", response)

if __name__ == "__main__":
  main()