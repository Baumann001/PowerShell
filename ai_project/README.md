# IA Conversacional que Fala

Este projeto cria uma IA conversacional que pode ouvir e falar em português, usando OpenAI GPT-3.5-turbo.

## Pré-requisitos

- Python 3.8 ou superior
- Conta na OpenAI com chave de API (obtenha em https://platform.openai.com/)

## Instalação

1. Clone ou baixe este repositório.

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```
   python -m venv venv
   venv\Scripts\activate  # No Windows
   # ou
   source venv/bin/activate  # No Linux/Mac
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Configure a chave da API do OpenAI:
   - Copie o arquivo `.env.example` para `.env`
   - Edite o arquivo `.env` e adicione sua chave da API:
     ```
     OPENAI_API_KEY=sua-chave-aqui
     ```

## Execução

Execute o chatbot:
```
python speech_chatbot.py
```

O chatbot irá ouvir sua voz, processar a entrada e responder falando.

## Uso

- Fale claramente em português brasileiro.
- Diga "sair" para encerrar a conversa.
- A IA mantém o contexto da conversa para respostas mais naturais.

## Troubleshooting

- **Problemas com PyAudio/SpeechRecognition:**
  - No Windows: Instale o Microsoft Visual C++ Build Tools.
  - Baixe o wheel compatível em https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
  - Instale com: `pip install caminho/para/o/arquivo.whl`

- **Erro na API do OpenAI:**
  - Verifique se a chave da API está correta no arquivo `.env`.
  - Certifique-se de que sua conta OpenAI tem créditos suficientes.

- **Microfone não detectado:**
  - Verifique as permissões do microfone no sistema.
  - Teste o microfone em outras aplicações.

## Melhorias Implementadas

- Uso do modelo GPT-3.5-turbo (mais atual e eficiente).
- Configuração segura da chave da API via variáveis de ambiente.
- Histórico de conversa para respostas contextuais.
- Tratamento de erros aprimorado.
- Interface em português.
