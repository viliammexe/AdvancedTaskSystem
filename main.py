from storage import TaskFileStorage
from engine import TaskProcessingEngine
import cli_interface

def run_system_app():
    storage = TaskFileStorage()
    engine = TaskProcessingEngine(storage)
    
    # Ukážkové dáta pre inicializáciu
    if not engine.tasks:
        engine.create_task("Finalize Documentation", "Complete the technical report", "high")
        engine.create_task("Verify API Integration", "Test GitHub search indexing", "medium")
    
    all_tasks = engine.tasks
    cli_interface.print_task_dashboard(all_tasks)

if __name__ == "__main__":
    run_system_app()