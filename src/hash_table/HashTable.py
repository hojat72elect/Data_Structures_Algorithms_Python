from typing import TypeVar, Generic, Tuple

from src.linked_list.SinglyLinkedList import SinglyLinkedList

K = TypeVar("K")
V = TypeVar("V")


class HashTable(Generic[K, V]):
    def __init__(self, capacity: int = 8):
        """
        Initialize the hash table with fixed buckets.
        Each bucket holds tuples of (key, value).
        """
        self._capacity = max(capacity, 1)
        self._size = 0
        self._buckets: list[SinglyLinkedList[Tuple[K, V]]] = [
            SinglyLinkedList[Tuple[K, V]]() for _ in range(self._capacity)
        ]

    def _hash(self, key: K) -> int:
        """
        Returns the index to the valid bucket.
        """
        return hash(key) % self._capacity  # We're using python's internal hash function

    def put(self, key: K, value: V):
        index = self._hash(key)
        bucket = self._buckets[index]

        current = bucket.head
        while current:
            existing_key, _ = current.data
            if existing_key == key:
                # key already exists in the table, we need to update the value
                current.data = (key, value)
                return
            current = current.next

        # The key doesn't exist in this bucket, write the new pair into the linkedlist
        bucket.append((key, value))
        self._size += 1

    def get(self, key: K) -> V:
        index = self._hash(key)
        bucket = self._buckets[index]

        current = bucket.head
        while current:
            k, v = current.data
            if k == key:
                return v
            current = current.next

        raise KeyError(f"Key not found: {key}")

    def remove(self, key: K) -> V:
        """
        Removes the key-value pair and returns the value
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        if not bucket.head:
            raise KeyError(f"Key not found: {key}")

        if bucket.head.data[0] == key:
            # key is in the head node of the bucket
            removed_pair = bucket.delete_head()
            self._size -= 1
            return removed_pair[1]

        # key is deeper in the linked list
        current = bucket.head
        while current.next:
            if current.next.data[0] == key:
                removed_pair = current.next.data
                current.next = current.next.next

                if current.next is None:
                    # we're removing the tail of the linked list
                    bucket.tail = current

                bucket._size -= 1
                self._size -= 1
                return removed_pair[1]

            current = current.next

        raise KeyError(f"Key not found: {key}")

    def contains(self, key: K) -> bool:
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def __setitem__(self, key: K, value: V) -> None:
        """Supports dictionary assignment syntax: ht["key"] = value"""
        self.put(key, value)

    def __getitem__(self, key: K) -> V:
        """Support dictionary lookup syntax: val = ht["key"]"""
        return self.get(key)

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        pairs = []
        for bucket in self._buckets:
            for key, val in bucket:
                pairs.append(f"{repr(key)}: {repr(val)}")
        return "{" + ", ".join(pairs) + "}"
