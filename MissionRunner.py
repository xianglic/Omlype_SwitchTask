from threadlevel.FlightScript import FlightScript
# Import derived tasks
from DetectTask import DetectTask

import queue



class MissionRunner(FlightScript):
    
    def __init__(self, drone, event_queue):
        super().__init__(drone)
        self.t1 = None
        self.t2 = None
        self.curr_task_id = None
        self.taskMap = {}
        self.event_queue = event_queue
    
    
    def define_task(self, event_queue):
        # Define task
        kwargs = {}
        # TASK1
        kwargs.clear()
        kwargs["gimbal_pitch"] = "-45.0"
        kwargs["drone_rotation"] = "0.0"
        kwargs["sample_rate"] = "2"
        kwargs["hover_delay"] = "5"
        kwargs["coords"] = "[{'lng': -80.0076661, 'lat': 40.4534506, 'alt': 15.0}, {'lng': -80.0075856, 'lat': 40.4526669, 'alt': 15.0}, {'lng': -80.0061211, 'lat': 40.4526995, 'alt': 15.0}, {'lng': -80.0057885, 'lat': 40.4536384, 'alt': 15.0}, {'lng': -80.0076661, 'lat': 40.4534506, 'alt': 15.0}]"
        self.t1 = DetectTask(self.drone, 1, event_queue, **kwargs)
        self.taskMap[1] = self.t1
        
        # TASK2
        kwargs.clear()
        kwargs["gimbal_pitch"] = "-45.0"
        kwargs["drone_rotation"] = "0.0"
        kwargs["sample_rate"] = "2"
        kwargs["hover_delay"] = "5"
        kwargs["coords"] = "[{'lng': -80.0076661, 'lat': 40.4534506, 'alt': 15.0}, {'lng': -80.0075856, 'lat': 40.4526669, 'alt': 15.0}, {'lng': -80.0061211, 'lat': 40.4526995, 'alt': 15.0}, {'lng': -80.0057885, 'lat': 40.4536384, 'alt': 15.0}, {'lng': -80.0076661, 'lat': 40.4534506, 'alt': 15.0}]"
        self.t2 = DetectTask(self.drone, 2, event_queue, **kwargs)
        self.taskMap[2] = self.t2
        
        
    
    def transit_to(self, task_id):
        self._kill()
        if (task_id != 0):
            self._push_task(self.taskMap[task_id])
            self._execLoop()
    
        
    def start_mission(self):
        # set the current task
        task_id = self.t1.get_task_id()
        self.set_currentTask(task_id)
        print(f"mission: current taskid:{task_id}\n")
        # start
        self.taskQueue.put(self.t1)
        self.drone.takeOff()
        self._execLoop()
        
    def set_currentTask(self, task_id):
        self.curr_task_id = task_id


 
    def run(self):
        try:
            # create the communication queue
            event_queue = queue.Queue()
            
            # define task
            print("define the tasks\n")
            self.define_task(event_queue)
            
            # start mission
            print("start the mission!\n")
            self.start_mission()
            
        except Exception as e:
            print(e)
            
