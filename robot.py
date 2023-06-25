import sys
from time import sleep
sys.path.append('C:\Program Files\CoppeliaRobotics\CoppeliaSimEdu\programming\zmqRemoteApi\clients\python')


class Robot:
    """
    A szimulációs környezetben létező robot irányításához tartozó osztály.
    """
    def __init__(self,sim) :
        """
        Az osztály konstruktora.

        Paraméter:
            sim:

        Létrehozott attribútumok:
        - sim: A szimulációt tartalmazó objektum
        - L_wheel: A bal oldali motornak a handle-je
        - R_wheel: A jobb oldali motornak a handle-je

        """
        self.sim = sim
        self.L_wheel = sim.getObjectHandle('/rightMotor')
        self.R_wheel = sim.getObjectHandle('/leftMotor')

    def execute_command(self,command_list):
        """
        Végigiterálja a parancsokat tartalmazó listát és annak megfelelően végrehajtsa a parancsot.

        Paraméter:
            command_list: Lista, ami tartalmazza az utasításokat.
        """
        for command in command_list:
            if command == 'előre':
                self.move_forward()
            if command == 'hátra':
                self.move_backward()
            if command == 'jobbra':
                self.move_right()
            if command == 'balra':
                self.move_left()

            self.stop_movement()
            pass

    def move_forward(self):
        """
        Beállítja a szimulációs környezetben létező robot bal és jobb oldali 
        kerekének sebességét és a robot előre megy.
        """
        self.sim.setJointTargetVelocity(self.L_wheel,2)
        self.sim.setJointTargetVelocity(self.R_wheel,2)
        sleep(3)

    def move_backward(self):
        """
        Beállítja a szimulációs környezetben létező robot bal és jobb oldali 
        kerekének sebességét és a robot hátra megy.
        """
        self.sim.setJointTargetVelocity(self.L_wheel,-2)
        self.sim.setJointTargetVelocity(self.R_wheel,-2)
        sleep(3)
            
    def move_left(self):
        """
        Beállítja a szimulációs környezetben létező robot bal és jobb oldali 
        kerekének sebességét és a robot balra fordul.
        """
        self.sim.setJointTargetVelocity(self.L_wheel,1)
        self.sim.setJointTargetVelocity(self.R_wheel,0)
        sleep(1.7)
    

    def move_right(self):
        """
        Beállítja a szimulációs környezetben létező robot bal és jobb oldali 
        kerekének sebességét és a robot jobbra.
        """
        self.sim.setJointTargetVelocity(self.L_wheel,0)
        self.sim.setJointTargetVelocity(self.R_wheel,1)
        sleep(1.7)
        

    def stop_movement(self):
        """
        Beállítja a szimulációs környezetben létező robot bal és jobb oldali 
        kerekének sebességét és a robot nem mozog.
        """
        self.sim.setJointTargetVelocity(self.L_wheel,0)
        self.sim.setJointTargetVelocity(self.R_wheel,0)

