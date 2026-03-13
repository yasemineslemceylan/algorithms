"""Greedy scheduling logic.

The goal is to build an order of tasks that is *good enough* using
simple greedy rules instead of trying all possible orders.

Greedy strategy used here:
1. Prefer tasks with **higher priority**.
2. If two tasks have the same priority, run the one with the
   **earlier deadline** first.
"""

from typing import List, Tuple

from .task import Task


def schedule_tasks(tasks: List[Task]) -> Tuple[List[Task], int]:
    """Return tasks in greedy order and total execution time.

    Args:
        tasks: list of Task objects to schedule.

    Returns:
        scheduled: new list of tasks in the chosen order.
        total_time: sum of all task durations.
    """

    # Greedy choice:
    #   - highest priority first  -> sort by negative priority
    #   - if tie, earliest deadline first
    scheduled = sorted(tasks, key=lambda t: (-t.priority, t.deadline))

    total_time = sum(t.duration for t in scheduled)
    return scheduled, total_time

