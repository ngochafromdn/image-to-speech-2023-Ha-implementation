
import pyttsx3
import IPython.display as ipd
import tempfile

class ReadingWord:
    def __init__(self, speed=1.0):
        self.speed = speed
        self.engine = pyttsx3.init()

    def read_aloud(self, word, lang='en'):
        with tempfile.NamedTemporaryFile(delete=True) as fp:
            self.engine.save_to_file(word, fp.name + ".mp3")
            self.engine.runAndWait()
            ipd.display(ipd.Audio(fp.name + ".mp3", autoplay=True))

