# Omlype_SwitchTask

Entrypoint of the project is start.py

Project overall logic:
The entry point will create two threads 
  a MissionRunner that helps create the task and run the current task as an individual thread.
  a TaskController that helps monitor the triggered event during executing the task, and transit the current task to another task based on triggered event.
  
Note: The DetectTask class is used to define the functionality of detect task.

Note: The threadlevel dir has FlightScript and Task class, which are basically parent class of Mission Runner and DetectTask

