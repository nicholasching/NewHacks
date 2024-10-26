from geminiRequestFramework import geminiRequestFramework
from ttsRequestFramework import ttsRequestFramework

gemini = geminiRequestFramework()
tts = ttsRequestFramework(0.5, 0.6)

gemini.uploadAudio()
tts.convertTTS(gemini.generateResponse())
