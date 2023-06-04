from loguru import logger
import pyttsx3
import logging

# Suppress logging done by pyttsx3
logging.getLogger('comtypes-_comobject').setLevel(logging.WARNING)

class VoiceAssistant:
    def __init__(self):
        logger.info("Initialize VA...")

        logger.info("Initialize Speech")
        self.tts = pyttsx3.init();

        voices = self.tts.getProperty('voices')
        for voice in voices:
            logger.info(voice)

        voiceID = """HKEY_LOCAL-MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0"""
        self.tts.setProperty('voice', voiceID)
        self.tts.say("Initialisierung abgeschlossen");
        self.tts.runAndWait();
        logger.debug("Sprachausgabeninitialisierung abgeschlossen.")

    def run(self):
        logger.info("VoiceAssistant Instanz wurde gestartet.")
        self.tts.say("Ich bin bereit.");
        self.tts.runAndWait();

if __name__ == '__main__':
    logger.info("Anwendung wurde gestartet.")
    va = VoiceAssistant()
    va.run()