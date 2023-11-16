import threading
from threadlevel.Task import Task
import time
import ast

class DetectTask(Task):

    def __init__(self, drone, task_id, event_queue,**kwargs):
        super().__init__(drone, task_id, **kwargs)
        self.event_queue = event_queue
        
    def trigger_event(self):
        self.event_queue.put((self.task_id,  "timeup"))

    def run(self):
        # construct the timer with 5 second
        timer = threading.Timer(5.0, self.trigger_event)
        # Start the timer
        timer.start()
        
        try:
            print("Detect Task: hi this is detect task\n")
            coords = ast.literal_eval(self.kwargs["coords"])
            self.drone.setGimbalPose(0.0, float(self.kwargs["gimbal_pitch"]), 0.0)
            hover_delay = int(self.kwargs["hover_delay"])
            for dest in coords:
                lng = dest["lng"]
                lat = dest["lat"]
                alt = dest["alt"]
                self.drone.moveTo(lat, lng, alt)
                print("Detect Task: move to\n")
                time.sleep(hover_delay)
        except Exception as e:
            print(e)

