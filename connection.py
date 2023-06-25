import sys

sys.path.append('C:\Program Files\CoppeliaRobotics\CoppeliaSimEdu\programming\zmqRemoteApi\clients\python')

from zmqRemoteApi import RemoteAPIClient

class ConnectionSetup():
    """
    Az osztály kezeli a szimulációs környezethez való csatlakozást.
    """
    
    def __init__(self):
        """
        Az osztály konstruktora.

        Létrehozott attribútumok:
        - client: RemoteAPIClient típusú objektum.
        - sim: Objektum, amely tartalmazza szimulációs környezet objektumát.
        """
        self.client = RemoteAPIClient()
        self.sim = self.client.getObject('sim')

    def start_simulation(self):
        """
        A szimuláció képkockáinak a inicializálására, valamint a szimuláció elindítására szolgál.

        Visszatérít:
        - sim: Szimulációs objektum, vagy None, ha a kapcsolat nem sikerült.
        """
        self.sim.setInt32Param(self.sim.intparam_idle_fps, 0)
        self.sim.startSimulation()
    
        return self.sim
        
        








