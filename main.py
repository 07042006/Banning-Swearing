import speech_recognition as sr
from plyer import notification

lulaCoins = 10

def remover_lulaCoins():
    global lulaCoins
    lulaCoins = lulaCoins - 1
    if lulaCoins <= 0:
        notification.notify(
        title="LULA COINS ZERADO",
        message="Seus lula coins foram zerados - Reiniciando PC",
        app_name="Banning Swearing"
        )


def enviar_notificacao(palavra):
    mensagem = f"Palavra identificada: {palavra}"
    notification.notify(
        title="Alerta de Palavra",
        message=mensagem,
        app_name="Identificador de Palavras"
    )

def verificar_palavras(texto, palavras):
    for palavra in palavras:
        if palavra in texto:
            return palavra
    return None

def main():
    with open('arquivo.txt', 'r') as arquivo:
        palavras_lista = [linha.strip() for linha in arquivo]

    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Ouvindo...")
                audio = recognizer.listen(source, timeout=10)

            texto = recognizer.recognize_google(audio, language="pt-BR").lower()
            print("Texto reconhecido:", texto)

            palavra_identificada = verificar_palavras(texto, palavras_lista)

            if palavra_identificada:
                enviar_notificacao(palavra_identificada)
                remover_lulaCoins();

        except sr.UnknownValueError:
            print("Não foi possível entender o áudio")
        except sr.RequestError as e:
            print(f"Erro ao fazer a requisição ao serviço de reconhecimento de voz; {e}")

if __name__ == "__main__":
    main()
