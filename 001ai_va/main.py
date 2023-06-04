from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, level="INFO")    # Logger Levels: TRACE, DEBUG, INFO, SUCCESS, WARNING, ERROR, CRITICAL

class VoiceAssistant:
    def __init__(self):
        logger.error("Initialize")

    def run(self):
        logger.debug("Run")

if __name__ == '__main__':
    va = VoiceAssistant()
    va.run()
    logger.info("Started")