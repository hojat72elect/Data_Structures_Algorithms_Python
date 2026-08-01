from typing import Generic, TypeVar, Optional, Generator

T = TypeVar("T")


class DoubleNode(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.next: Optional["DoubleNode[T]"] = None
        self.previous: Optional["DoubleNode[T]"] = None


class DoublyLinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[DoubleNode[T]] = None
        self.tail: Optional[DoubleNode[T]] = None
        self._size: int = 0

    def append(self, data: T):
        new_node = DoubleNode(data)

        if not self.head:
            # list is currently empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def prepend(self, data: T):
        new_node = DoubleNode(data)

        if not self.head:
            # list is currently empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

        self._size += 1

    def insert(self, index: int, data: T):
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.prepend(data)
            return

        if index == self._size:
            self.append(data)
            return

        new_node = DoubleNode(data)
        current_node: DoubleNode[T] | None = None

        # optimized traversal - search from head or tail, depending on index proximity
        if index < self._size // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self._size - 1 - index):
                current_node = current_node.previous

        # The new-node should be inserted before the current_node
        new_node.previous = current_node.previous
        new_node.next = current_node
        current_node.previous.next = new_node
        current_node.previous = new_node

        self._size += 1

    def delete_head(self) -> T:
        """
        Deletes and returns the head's content
        """
        if not self.head:
            raise IndexError("The list is empty")

        result = self.head.data
        self.head = self.head.next
        self._size -= 1

        if self.head is None:
            # The list only had 1 item, tail should be updated as well
            self.tail = None
        else:
            self.head.previous = None

        return result

    def delete_tail(self) -> T:
        """
        Deletes and returns the tail's content.
        """
        if not self.head or not self.tail:
            raise IndexError("The list is empty")

        result = self.tail.data
        self.tail = self.tail.previous
        self._size -= 1

        if self.tail is None:
            # The list only had 1 item, head should be updated as well
            self.head = None
        else:
            self.tail.next = None

        return result

    def __iter__(self) -> Generator[T, None, None]:
        """Support iteration forward over values directly (e.g., in `for x in list`)."""
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        elements = [str(val) for val in self]
        return "None <-> " + " <-> ".join(elements) + " <-> None" if elements else "Empty List"
