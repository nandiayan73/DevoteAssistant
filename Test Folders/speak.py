import speech_recognition as sr

recognizer = sr.Recognizer()

# List all microphones
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Microphone with name '{name}' found for `Microphone(device_index={index})`")

# Use the correct microphone
with sr.Microphone(device_index=1) as source:
    print("Please say something:")
    audio = recognizer.listen(source)
    # Continue with your code...
