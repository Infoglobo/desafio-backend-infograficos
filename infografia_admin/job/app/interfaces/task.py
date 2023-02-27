from abc import ABC, abstractmethod


class ITask(ABC):
    @abstractmethod
    async def do_task(self) -> None:
        ...
