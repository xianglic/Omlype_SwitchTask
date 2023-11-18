import queue
from MissionRunner import MissionRunner
from ParrotAnafi import ParrotAnafi
from TaskController import TaskController

if __name__ == "__main__":
    
    # connect the drone
    args = {'ip': '10.202.0.1'}
    drone = ParrotAnafi(**args)
    if not drone.isConnected():
        drone.connect()
        print("connect the drone\n")
        
    # init the mission runner
    mr = MissionRunner(drone)
    print("init the mission runner\n")
    
    # context switch controller
    tc =  TaskController(mr)
    print("init the task switch controller\n")

    
    # running the program
    print("run the flight mission\n")
    tc.start()
    mr.start()
    
    
    tc.join()
    mr.join()
    