from rich.progress import Progress

import time

tasks = {
    'task1': 2.5,
    'task2': 1.5,
    'task3': 0.5,
    'task4': 1.5,  
    'task5': 1,  
}

with Progress() as progress:
    for task in progress.track(tasks, description="doing tasks..."):
        progress.console.print(f"do {task}")
        time.sleep(int(tasks[task]))