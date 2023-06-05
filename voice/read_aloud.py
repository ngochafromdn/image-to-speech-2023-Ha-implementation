from gtts import gTTS
import pygame
import tempfile

class ReadingWord:
    def __init__(self, speed=1.0):
        self.speed = speed
        self.engine = None
        
        # Initialize pygame mixer
        pygame.mixer.init()

    def read_aloud(self, word, lang='en'):
        tts = gTTS(text=word, lang=lang)
        
        with tempfile.NamedTemporaryFile(delete=True) as fp:
            tts.save(fp.name + ".mp3")
            
            # Load and play the audio using pygame mixer
            pygame.mixer.music.load(fp.name + ".mp3")
            pygame.mixer.music.play()
            
            # Wait until the audio finishes playing
            while pygame.mixer.music.get_busy():
                pass
