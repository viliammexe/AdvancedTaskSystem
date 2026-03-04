from models import CoreTask
from datetime import datetime

class TaskProcessingEngine:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self._initialize_tasks()

    def _initialize_tasks(self):
        raw_data = self.storage.load_all()
        return [CoreTask(**t) for t in raw_data]

    def create_task(self, title, desc, priority="medium"):
        new_id = len(self.tasks) + 1
        new_task = CoreTask(
            id=new_id,
            title=title,
            description=desc,
            priority=priority,
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        self.tasks.append(new_task)
        self.storage.save_all([t.to_dict() for t in self.tasks])
        return new_id

    def list_by_priority(self, level):
        return [t for t in self.tasks if t.priority == level]