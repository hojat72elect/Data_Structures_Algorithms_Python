from src.SinglyLinkedList import Node, SinglyLinkedList


class TestNode:
    def test_node_initialization(self):
        node = Node(19)
        assert node.data == 19
        assert node.next is None


class TestSinglyLinkedList:
    def test_simple_list_behavior(self):
        sut: SinglyLinkedList[int] = SinglyLinkedList()
        assert sut.head is None
        assert sut.tail is None
        assert len(sut) == 0
        assert str(sut) == "Empty List"

        sut.append(10)
        assert len(sut) == 1
        assert sut.head is not None
        assert sut.head.data == 10
        assert sut.head is sut.tail
        assert str(sut) == "10 -> None"

        sut.prepend(20)
        sut.append(30)
        assert len(sut) == 3
        assert list(sut) == [20, 10, 30]
        assert str(sut) == "20 -> 10 -> 30 -> None"
