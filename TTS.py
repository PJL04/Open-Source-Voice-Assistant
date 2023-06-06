import time, pyttsx3
import multiprocessing

def __speak__(text, voiceID):
    engine = pyttsx3.init()
    engine.setProperty('vocie', voiceID)
    engine.say(text)
    engine.runAndWait()



class Voice:

    def __init__(self):
        self.process = None
        self.voiceID = """HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0"""

    def say(self, text):
        if self.process:
            self.stop()

        p = multiprocessing.Process(target=__speak__, args=(text, self.voiceID))
        p.start()
        self.process = p

    def set_voice(self, voiceID):
        self.voiceID = voiceID

    def stop(self):
        if self.process:
            self.process.terminate()

    def get_voice_keys_by_language(self, language=''):
        result = []
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        lang_search_str = language.upper()+"-"

        for voice in voices:
            if language == '':
                result.append(voice.id)
            elif lang_search_str in voice.id:
                result.append(voice.id)

        return result