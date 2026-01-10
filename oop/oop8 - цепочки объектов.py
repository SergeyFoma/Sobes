class Task:
    def __init__(self, name):
        self.name=name 
        self.next=None

    def add_next(self, task):
        self.next=task 

task1=Task("One the Task")
task2=Task("Two the Task")
task3=Task("Three the Task")

# task1.add_next(task3)
# task2.add_next(task2)
# task3.add_next(task1)

current_task=task1
while True:
    print(current_task.name)
    current_task=current_task.next
    if current_task is None:
        break 
#print(task1.next.name)
