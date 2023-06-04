
import pyttsx3

class ReadingWord:
    def __init__(self, speed=150):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', speed)  # Speed of speech

    def read_aloud(self, word):
        self.engine.say(word)
        self.engine.runAndWait()

if __name__ == "__main__":
    reader = ReadingWord(speed=200)  # Specify the speed parameter here
    word = "Xin chào!"
    reader.read_aloud(word)
