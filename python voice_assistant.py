import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop to listen for commands
while True:
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        text = r.recognize_google(audio)
        print("You said: " + text)

        # Process the command and respond back
        if "hello" in text:
            speak("Hello, how are you?")
        elif "goodbye" in text:
            speak("Goodbye!")
            break
        else:
            speak("I didn't understand what you said.")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
