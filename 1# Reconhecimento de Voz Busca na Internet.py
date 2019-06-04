import speech_recognition as sr
#Reconhecimento de voz
import requests
from bs4 import BeautifulSoup
#Importa a Requests e a bs para baixar paginas
from unicodedata import normalize
#"decodifica acentos"
from gtts import gTTS
from playsound import playsound

"""Este "programa" apenas escuta,reconhece e interpreta o que foi dito, baseando-se
nisso, caso a mensagem dita corresponda a alguma das que foi programada o programa toma as
devidas decisões """
lista = []
def mic():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Escutando: ", end="")
        audio = microfone.listen(source)
        frase = microfone.recognize_google(audio,language='pt-BR')
        print(frase) 
        if frase == "Olá Jarvis":
            print("Olá mestre")
        entrada2 = frase.replace(' ', '%20')
        entrada3 =  normalize('NFKD', entrada2).encode('ASCII', 'ignore').decode('ASCII')
        if entrada3[0:14] == "O%20que%20e%20":
            print("Buscando resultados... ")
            pagina = requests.get("https://www.dicio.com.br/"+entrada3[14:len(entrada3)]+"/")
            soup = BeautifulSoup(pagina.content, 'html.parser')
            for i in range(0,1):
                conteudo = soup.find("p").get_text()
                lista.append(conteudo)
            #print("Seu resultado: ")
            #print(lista)
            lista2 = str(lista).strip('[]')
            tts = gTTS(lista2, lang="pt-br")
            tts.save("hello.mp3")
            playsound("hello.mp3")
mic()
