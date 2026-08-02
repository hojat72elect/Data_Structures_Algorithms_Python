from src.queue.Queue import Queue


class TestQueue:
    def test_simple_queue_behavior(self):
        sut = Queue[int]()

        assert sut.is_empty() is True

        sut.enqueue(23)
        sut.enqueue(64)
        sut.enqueue(41)

        assert str(sut) == "Front -> 23 -> 64 -> 41 <- Back"
        assert len(sut) == 3
        assert sut.peek() == 23
        assert sut.dequeue() == 23
        assert sut.dequeue() == 64
        assert sut.dequeue() == 41

        assert sut.is_empty() is True
