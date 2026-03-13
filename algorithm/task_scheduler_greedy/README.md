# Task Scheduler using Greedy Algorithm

Beginner‑friendly Python console project that schedules tasks using a simple **greedy algorithm** based on **priority** and **deadline**.

## Project structure

```
task_scheduler_greedy/
├── main.py       # Console menu and user interaction
├── scheduler.py  # Greedy scheduling logic
├── task.py       # Task model
└── README.md
```

## Project description

The program lets you:

- Add tasks with:
  - name
  - duration
  - deadline
  - priority
- View the list of tasks.
- Run a **greedy scheduler** that orders tasks.
- See:
  - execution order
  - start and finish time of each task
  - whether the task meets its deadline
  - total execution time.

Everything runs in the **terminal / console** with a simple text menu.

## Algorithm explanation

We use a basic **greedy strategy**:

1. **Higher priority first**  
   Tasks with a larger `priority` value are considered more important.
2. **Earlier deadline first (tie‑breaker)**  
   If two tasks have the same priority, we run the task with the **earlier deadline** first.

Implementation (in words):

- Put all tasks into a list.
- Sort the list using the key `(-priority, deadline)`.
  - The minus sign means **higher priority comes first**.
  - Smaller deadline values come first.
- Walk through the sorted list and accumulate the current time to compute:
  - start time
  - finish time
  - whether `finish_time <= deadline`.

This greedy algorithm is:

- **Fast**: sorting takes \(O(n \log n)\).
- **Simple**: easy to understand for a second‑year student.
- **Not always globally optimal**, but often good enough in practice.

## Technologies used

- **Python 3**
- Only **basic standard features**:
  - lists
  - simple classes
  - functions
  - loops and conditionals

No external libraries are required.

## How to run the project

1. Open a terminal.
2. Go to the project folder:

   ```bash
   cd task_scheduler_greedy
   ```

3. Run the program:

   ```bash
   python main.py
   ```

4. Use the menu:

   - `1` – Add task  
   - `2` – View tasks  
   - `3` – Run scheduler  
   - `4` – Exit

## Example output

Example session (user input is after `>`):

```text
=== Task Scheduler (Greedy) ===
1. Add task
2. View tasks
3. Run scheduler
4. Exit
Choose an option (1-4): > 1

--- Add Task ---
Task name: > Study algorithms
Duration (time units): > 3
Deadline (time units from now): > 5
Priority (higher number = more important): > 2
Task added.

=== Task Scheduler (Greedy) ===
1. Add task
2. View tasks
3. Run scheduler
4. Exit
Choose an option (1-4): > 1

--- Add Task ---
Task name: > Play games
Duration (time units): > 2
Deadline (time units from now): > 10
Priority (higher number = more important): > 1
Task added.

=== Task Scheduler (Greedy) ===
1. Add task
2. View tasks
3. Run scheduler
4. Exit
Choose an option (1-4): > 3

--- Greedy Schedule ---
1. Study algorithms | start=0, finish=3, deadline=5, priority=2 -> OK
2. Play games       | start=3, finish=5, deadline=10, priority=1 -> OK

Total execution time: 5 time units.
```

You can change durations, deadlines and priorities to see how the schedule changes.

