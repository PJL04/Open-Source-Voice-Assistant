from loguru import logger
import pyttsx3
from TTS import Voice
import multiprocessing


class VoiceAssistant:
    def __init__(self):
        logger.info("Initialize VA...")

        logger.info("Initialize Speech")
        self.tts = Voice()

        voices = self.tts.get_voice_keys_by_language("German")

        if len(voices) > 0:
            logger.info('Stimme {} gesetzt.', voices[0])
            self.tts.set_voice(voices[0])
        else:
            logger.warning("Es wurden keine Stimmen gefunden.")

        self.tts.say("Initialisierung abgeschlossen")
        logger.debug("Sprachausgabe initialisiert")


    def run(self):
        logger.info("VoiceAssistant-Instanz wurde gestartet.")

if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    logger.info("Anwendung wurde gestartet.")
    va = VoiceAssistant()
    va.run()