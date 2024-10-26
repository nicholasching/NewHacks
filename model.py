from geminiRequestFramework import geminiRequestFramework
from ttsRequestFramework import ttsRequestFramework

class model:
    gemini = geminiRequestFramework()
    tts = ttsRequestFramework(0.5, 0.6)

    def generateResponse(self, audioPath):
        model.gemini.uploadAudio(audioPath)
        return model.tts.convertTTS(model.gemini.generateResponse())
    
    def __init__(self):
        pass
