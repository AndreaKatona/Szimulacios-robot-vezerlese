import PySimpleGUI as sg
from connection import ConnectionSetup
from robot import Robot

class Interface:

    def __init__(self, speech_recognizer):
        """
        Az osztály konstruktora.

        Paraméterek:
            speech_recognizer: beszédfelismerő (SpeechRecognizer) objektum
           
        Létrehozott attribútumok:
        - speech_recognizer: beszédfelismerő objektum
        - connection: Objektum a szimulációs környezethez való csatlakozáshoz
        - layout: a felhasználói felületen az elemek elrendezése
        - window: a felhasználói felület ablaka

        """

        self.speech_recognizer = speech_recognizer
        self.connection = ConnectionSetup()
        sg.theme('NeutralBlue')

        self.layout = [[sg.Text('Beszélt szöveg:')],
                       [sg.Output(size=(60, 10))],
                       [sg.Button('Szimulacio inditasa',key='SIM-START'),sg.Button('Szimulacio leállítása',key='SIM-STOP',disabled=True)],
                       [sg.Button('Felvétel indítása', key='START',disabled=True), sg.Button('Felvétel leállítása', key='STOP', disabled=True), sg.Button('Kilépés', key='EXIT')]]

        self.window = sg.Window('Vezérlő alkalmazás', self.layout)

    def run(self):
        """
        A felhasználói felület futtatása.
        Amig a felület ablaka nincs lezárva figyeli az eseményeket és kezeli a gombnyomásokat.

        Események:
        - WINDOW_CLOSED: A felhasználó lezárja az ablakot, a felismerés lezárúl.
        - EXIT: A felhasználó a 'Kilépés' gombra kattintott, a felismerés lezárúl és kilép.
        - CON-START: A felhasználó a 'Szimulacio inditasa' gombra kattintott és elindítja a szimulációt.
        - CON-STOP: A felhasználó a 'Szimulacio leállítása' gombra kattintott és leállítja a szimulációt.
        - START: A felhasználó a 'Felvétel indítása' gombra kattintott és elindul a beszédfelismerés.
        - STOP: A felhasználó a 'Felvétel leállítása' gombra kattintott és leállítja a beszédfelismerést.

        """
        while True:

            event, _ = self.window.read(timeout=100)

            if event == sg.WINDOW_CLOSED or event == 'EXIT':
                self.speech_recognizer.stop()
                self.sim.stopSimulation()
                break
            if event == 'SIM-START':
                self.sim = self.connection.start_simulation()
               
               
                self.robot = Robot(self.sim)
                self.window.Element('SIM-START').Update(disabled=True)
                self.window.Element('SIM-STOP').Update(disabled=False)
                self.window.Element('START').Update(disabled=False)
                
                    
            if event == 'SIM-STOP':

                self.sim.stopSimulation()
                self.window.Element('SIM-START').Update(disabled=False)
                self.window.Element('SIM-STOP').Update(disabled=True)
                self.window.Element('START').Update(disabled=True)
                self.window.Element('STOP').Update(disabled=True)

            if event == 'START':
                self.speech_recognizer.start()
                self.window.Element('SIM-STOP').Update(disabled=True)
                self.window.Element('START').Update(disabled=True)
                self.window.Element('STOP').Update(disabled=False)

            if event == 'STOP':
                self.speech_recognizer.stop()
                self.window.Element('SIM-STOP').Update(disabled=False)
                self.window.Element('START').Update(disabled=False)
                self.window.Element('STOP').Update(disabled=True)

            if self.speech_recognizer.data_available.isSet():
                command=self.speech_recognizer.getLatestCommand()
                if command:
                    self.robot.execute_command(command)
           
           
        self.window.close()

