import json
import os

class TaskFileStorage:
    def __init__(self, filename="task_records.json"):
        self.filename = filename

    def save_all(self, data_list):
        with open(self.filename, 'w') as f:
            json.dump([item for item in data_list], f, indent=4)

    def load_all(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as f:
            return json.load(f)