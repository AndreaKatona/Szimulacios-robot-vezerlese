from speech import SpeechRecognizer
from user_interface import Interface


if __name__ == '__main__':
     """
     Ez a főprogram belépési pontja.
     Inicializálja a felhasználói felületet és a beszédfelismerőt,
     majd elindítja a felhasználói felületet.
     """
     speech_recognizer = SpeechRecognizer()
     interface = Interface(speech_recognizer)
     interface.run()
   