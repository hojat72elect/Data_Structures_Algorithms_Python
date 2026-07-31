from typing import Generic, TypeVar, Optional

T = TypeVar("T")  # generic type


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.next: Optional["Node[T]"] = None


class SinglyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self._size: int = 0

    def append(self, data: T) -> None:
        new_node = Node(data)

        if not self.head:
            # list is currently empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def prepend(self, data: T) -> None:
        new_node = Node(data)

        if not self.head:
            # list is currently empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self._size += 1

    def insert(self, index: int, data: T) -> None:
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.prepend(data)
            return

        if index == self._size:
            self.append(data)
            return

        new_node = Node(data)
        current_node = self.head
        for _ in range(index - 1):
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node
        self._size += 1

    