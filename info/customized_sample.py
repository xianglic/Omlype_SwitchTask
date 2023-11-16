
from __future__ import annotations
from abc import ABC, abstractmethod


# The common state interface for all the states
class State(ABC):
    @property
    def drone(self) -> Drone:
        return self._drone

    @drone.setter
    def drone(self, drone: Drone) -> None:
        self._drone = drone

    @abstractmethod
    def transit(self) -> None:
        pass

    @abstractmethod
    def finish(self) -> None:
        pass

# The Elevator class is the context. It should be initiated with a default state.
class Drone:

    _state = None

    def __init__(self, state: State) -> None:
        self.setDrone(state)

    # method to change the state of the object
    def setDrone(self, state: State):

        self._state = state
        self._state.drone = self

    def presentState(self):
        print(f"Drone is in {type(self._state).__name__}")

    # the methods for executing the elevator functionality. These depends on the current state of the object.
    def transit(self):
        self._state.transit()

    def finish(self):
        self._state.finish()





# The concrete states
# We have two states of the elevator: when it is on the First floor and the Second floor
class detectState(State):

    # If the down button is pushed when it is already on the first floor, nothing should happen
    def transit(self) -> None:
        self.drone.setDrone(trackState())
        print("detect the yellow hat, transit the state from detect to track")

    # if up button is pushed, move upwards then it changes its state to second floor.
    def finish(self) -> None:
        self.drone.setDrone(finishedState())
        print("flight done")


class trackState(State):

    # if down button is pushed it should move one floor down and open the door
    def transit(self) -> None:
        self.drone.setDrone(detectState())
        print("time out, transit to the detect state")
        
    def finish(self) -> None:
        print("done")
        
class finishedState(State):
    def transit(self) -> None:
        print("done")

    def finish(self) -> None:
        print("done")
       
       
       
def getState(drone: Drone) -> State:
    return drone._state  # returns the current state of the drone

def detectTask():
    print("Performing detect task...")
    print("self.cloudlet.switchModel(\"coco\")")
    print("self.drone.setGimbalPose(0.0, 20, 0.0)")
    print("move()")

def trackTask():
    print("Performing track task...")
    

if __name__ == "__main__":
    # The client code.
    myDrone = Drone(detectState())
    myDrone.presentState()

    # Up button is pushed
    myDrone.transit()

    myDrone.presentState()
    
    while(1):
        currState = getState(myDrone)
        if (currState == detectState):
            detectTask()
        elif (currState == trackState):
            trackTask()
            

