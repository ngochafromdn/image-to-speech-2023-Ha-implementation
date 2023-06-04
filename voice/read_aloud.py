
from gtts import gTTS
import tempfile
import IPython.display as ipd

class ReadingWord:
    def __init__(self, speed=1.0):
        self.speed = speed

    def read_aloud(self, word, lang='en'):
        tts = gTTS(text=word, lang=lang)
        with tempfile.NamedTemporaryFile(delete=True) as fp:
            tts.save(fp.name + ".mp3")
            ipd.display(ipd.Audio(fp.name + ".mp3", autoplay=True))

