"""Console application: Task Scheduler using Greedy Algorithm.

The user can add tasks with:
    - name
    - duration
    - deadline
    - priority

Then the program uses a greedy strategy to build a schedule:
    1) Always pick the task with **highest priority**.
    2) If priorities are equal, pick the task with the **earlier deadline**.

This is not always the globally optimal schedule, but it is simple,
fast, and works well in many real situations.
"""

from typing import List

from scheduler import schedule_tasks
from task import Task


def ask_int(prompt: str) -> int:
    """Ask the user for an integer, repeat until valid."""
    while True:
        raw = input(prompt)
        try:
            value = int(raw)
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")


def add_task(tasks: List[Task]) -> None:
    """Create a new Task from user input and add it to the list."""
    print("\n--- Add Task ---")
    name = input("Task name: ").strip()
    if not name:
        print("Name cannot be empty. Task not added.")
        return

    duration = ask_int("Duration (time units): ")
    deadline = ask_int("Deadline (time units from now): ")
    priority = ask_int("Priority (higher number = more important): ")

    task = Task(name=name, duration=duration, deadline=deadline, priority=priority)
    tasks.append(task)
    print("Task added.\n")


def view_tasks(tasks: List[Task]) -> None:
    """Print all tasks in the order they were added."""
    print("\n--- Current Tasks ---")
    if not tasks:
        print("No tasks added yet.\n")
        return

    for idx, t in enumerate(tasks, start=1):
        print(
            f"{idx}. {t.name} | duration={t.duration}, "
            f"deadline={t.deadline}, priority={t.priority}"
        )
    print()


def run_scheduler(tasks: List[Task]) -> None:
    """Run the greedy scheduler and display the result."""
    print("\n--- Greedy Schedule ---")
    if not tasks:
        print("No tasks to schedule. Add some tasks first.\n")
        return

    scheduled, total_time = schedule_tasks(tasks)

    current_time = 0
    for idx, t in enumerate(scheduled, start=1):
        start_time = current_time
        finish_time = current_time + t.duration
        # A task meets its (simple) deadline if we finish before or at the deadline.
        meets_deadline = finish_time <= t.deadline
        status = "OK" if meets_deadline else "LATE"

        print(
            f"{idx}. {t.name} | start={start_time}, finish={finish_time}, "
            f"deadline={t.deadline}, priority={t.priority} -> {status}"
        )

        current_time = finish_time

    print(f"\nTotal execution time: {total_time} time units.\n")


def main() -> None:
    tasks: List[Task] = []

    menu = (
        "\n=== Task Scheduler (Greedy) ===\n"
        "1. Add task\n"
        "2. View tasks\n"
        "3. Run scheduler\n"
        "4. Exit\n"
    )

    while True:
        print(menu)
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            run_scheduler(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()

