import os
import speech_recognition as sr
import pyttsx3
import openai
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar a chave da API do OpenAI a partir da variável de ambiente
openai.api_key = os.getenv('OPENAI_API_KEY')

# Inicializar o reconhecimento de voz
recognizer = sr.Recognizer()

# Inicializar o mecanismo de texto para fala
engine = pyttsx3.init()

# Contexto da conversa para manter o histórico
conversation_context = ""

def listen():
    with sr.Microphone() as source:
        print("Ouvindo...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='pt-BR')  # Português
            print(f"Você disse: {text}")
            return text
        except sr.UnknownValueError:
            print("Desculpe, não entendi.")
            return None
        except sr.RequestError:
            print("Desculpe, o serviço de voz está indisponível.")
            return None

def think_and_respond(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt,
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Erro na API do OpenAI: {e}")
        return "Desculpe, não consegui processar sua solicitação."

def speak(text):
    engine.say(text)
    engine.runAndWait()

def main():
    global conversation_context
    print("IA Conversacional Iniciada. Diga 'sair' para parar.")
    while True:
        user_input = listen()
        if user_input:
            if user_input.lower() == 'sair':
                speak("Até logo!")
                break
            # Atualizar o contexto da conversa
            conversation_context += f"Usuário: {user_input}\n"
            messages = [
                {"role": "system", "content": "Você é um assistente amigável que responde em português."},
                {"role": "user", "content": conversation_context}
            ]
            # Gerar resposta usando IA
            response = think_and_respond(messages)
            print(f"IA: {response}")
            speak(response)
            conversation_context += f"IA: {response}\n"

if __name__ == "__main__":
    main()
