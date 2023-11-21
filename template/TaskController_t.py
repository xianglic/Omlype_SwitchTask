import threading


class TaskController(threading.Thread):
        
    
    def __init__(self, mr):
        super().__init__()
        self.mr = mr
        
        self.event_queue = mr.event_queue
        
        self.transitMap = {
            1: self.task_1_transit,
            2: self.task_2_transit
        }
        
    @staticmethod
    def task_1_transit(triggered_event):
        if (triggered_event == "timeup"):
            return "t2"
        if (triggered_event == "done"):
            return "terminate"
    @staticmethod
    def task_2_transit(triggered_event):
        if (triggered_event == "done"):
            return "terminate"
        
    @staticmethod
    def default_transit(triggered_event):
        print(f"no matched up transition, triggered event {triggered_event}\n", triggered_event)
        
        
    def next_task(self, triggered_event):
        current_task_id = self.mr.get_current_task()
        next_task_id  = self.transitMap.get(current_task_id, self.default_transit)(triggered_event)
        self.mr.transit_to(next_task_id)
        return next_task_id
    
    def run(self):
        print("hi start the controller\n")
        # check the triggered event
        while True:
            item = self.event_queue.get()
            if item is not None:
                print(f"Controller: Trigger one event {item} \n")
                print(f"Controller: Task id  {item[0]} \n")
                print(f"Controller: event   {item[1]} \n")
                if (item[0] == self.mr.get_current_task()):
                    next_task_id = self.next_task(item[1])
                    if (next_task_id == 0):
                        print(f"Controller: the current task is done, terminate the controller \n")
                        break

               
                

                
