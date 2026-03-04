def print_task_dashboard(tasks):
    print("=" * 30)
    print(" SYSTEM TASK DASHBOARD ")
    print("=" * 30)
    for t in tasks:
        status = "DONE" if t.is_completed else "OPEN"
        print(f"[{status}] {t.id}: {t.title} | Priority: {t.priority}")
    print("-" * 30)