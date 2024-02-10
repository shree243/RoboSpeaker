import pyttsx3

def pronounce(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    command = input("Enter the command you want to pronounce: ")
    pronounce(command)
