from typing import TypeVar, Generic

from src.linked_list.SinglyLinkedList import SinglyLinkedList

T = TypeVar("T")


class Queue(Generic[T]):
    def __init__(self):
        self._list: SinglyLinkedList[T] = SinglyLinkedList[T]()

    def is_empty(self) -> bool:
        return len(self._list) == 0

    def enqueue(self, data: T):
        self._list.append(data)

    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self._list.delete_head()

    def peek(self) -> T:
        """
        Returns the item at the front of the queue (without removing it).
        """
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        return self._list.head.data

    def __len__(self) -> int:
        return len(self._list)

    def __str__(self) -> str:
        if self.is_empty():
            return "Queue(empty)"
        elements = [str(val) for val in self._list]
        return f"Front -> {' -> '.join(elements)} <- Back"
