"""Simple Task model for the greedy scheduler."""


class Task:
    """
    Represents a single task.

    Attributes:
        name (str): Short name or description of the task.
        duration (int): How long the task takes (in time units).
        deadline (int): When the task should ideally be finished.
        priority (int): Higher value means more important.
    """

    def __init__(self, name: str, duration: int, deadline: int, priority: int) -> None:
        self.name = name
        self.duration = duration
        self.deadline = deadline
        self.priority = priority

    def __repr__(self) -> str:
        return (
            f"Task(name={self.name!r}, duration={self.duration}, "
            f"deadline={self.deadline}, priority={self.priority})"
        )

