pip install SpeechRecognition
#baixar a versão adequada do PyAudio de {https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio}
#--> Esta etapa é relativa a arquitetura do PC logo o download da Biblioteca PyAudio é feita de modo manual
#pip install "diretório + nome do arquivo .whl"
#https://medium.com/brasil-ai/reconhecimento-voz-python-35a5023767ca
#pip install gTTS (serviço de transformação TextToSpeech)  
#pip install playsound (toca sons)
#from gtts import gTTS
#from playsound import playsound

import speech_recognition as sr

def mic():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)
        frase = microfone.recognize_google(audio,language='pt-BR')
        print(frase)
        if frase == "Olá tudo bem":
            print("Olá, comigo está tudo certo!")
mic()
