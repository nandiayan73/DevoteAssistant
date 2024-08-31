import google.generativeai as genai
from dotenv import load_dotenv
import os
import subprocess
import json
import intro

load_dotenv()


# VARIABLES:
commads={
   "shell":0,
   "music":0,

}

# FUNCTIONS:
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


# GEMINI FUNCTIONS:
def create_chat_session():
  """Creates a new chat session with themodel="gemini-3.5-turbo" Gemini API."""
  return genai.ChatSession(model = genai.GenerativeModel('gemini-1.5-flash'))  

def send_message(chat_session, message):
  """Sends a message to the chat session and returns the response."""
  response = chat_session.send_message(message)
  return response.text

def run_shell_command(command,chat_session):
    try:
        # Validate that the command is not empty or improperly formatted
        if not command.strip():
            print("No command provided to execute.")
            return
        
        # Debugging: Print the command to be executed
        print(f"Executing command: {command}")

        # Execute the command
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Command Output:", result.stdout.decode())
        response=send_message(chat_session,"Well done, now tell the user about the command you provided and what it performed")
        return response
    except subprocess.CalledProcessError as e:
        print("Error executing command:", e.stderr.decode())


def main():
  
  # Replace with your API key
  genai.configure(api_key=os.environ["API_KEY"])

  chat_session = create_chat_session()
  send_message(chat_session,intro.first_input)
  while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
      break
    
    response = send_message(chat_session, user_input)
    output=response

    # run shell commands:
    response = send_message(chat_session, "If the user is asking for any work that you can do with the help of terminal, just write 'shell' , exactly like this no front or back space just only write shell and nothing")
    print(response.strip())
    if(response.strip()=="shell"):
        print("Entering shell command mode")
        response = send_message(chat_session, "Now you have to give the command only which will work,reply with the command only that will solve the user's problem,otherwise it will not run and error will occur,remember this time you have to give the desired command!")
        response=run_shell_command(response.strip(),chat_session)
        send_message(chat_session, "well done, now be careful what the user is asking, if he is asking for further shell commands to run do what you were told, otherwise reply by yourself")
        print(response)
        continue
    else:
       response=output
       print("No shell command mode")
    print("Govinda:", response)

# driver code
if __name__ == "__main__":
  main()