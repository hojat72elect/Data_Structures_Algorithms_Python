from src.linked_list.DoublyLinkedList import DoubleNode, DoublyLinkedList


class TestDoubleNode:
    def test_double_node_initialization(self):
        sut = DoubleNode(89)
        assert sut.data == 89
        assert sut.next is None
        assert sut.previous is None


class TestDoublyLinkedList:
    def test_simple_list_behavior(self):
        sut: DoublyLinkedList[int] = DoublyLinkedList()

        assert len(sut) == 0
        assert sut.head is None
        assert sut.tail is None
        assert str(sut) == "Empty List"

        sut.prepend(10)
        sut.append(20)
        sut.prepend(30)
        sut.append(40)

        assert list(sut) == [30, 10, 20, 40]
        assert len(sut) == 4
        assert sut.head.data == 30
        assert sut.tail.data == 40

        sut.insert(2, 45)
        assert list(sut) == [30, 10, 45, 20, 40]
