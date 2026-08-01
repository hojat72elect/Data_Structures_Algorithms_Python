from typing import TypeVar, Generic

from src.linked_list.SinglyLinkedList import SinglyLinkedList

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self):
        self._list: SinglyLinkedList[T] = SinglyLinkedList[T]()

    def is_empty(self) -> bool:
        return len(self._list) == 0

    def push(self, item: T):
        self._list.prepend(item)

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._list.delete_head()

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._list.head.data

    def __len__(self) -> int:
        return len(self._list)

    def __str__(self) -> str:
        if self.is_empty():
            return "Empty Stack"
        items = " -> ".join(str(val) for val in self._list)
        return f"Stack: Top -> {items}"
