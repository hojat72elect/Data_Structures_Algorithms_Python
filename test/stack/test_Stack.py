from src.stack.Stack import Stack


class TestStack:
    def test_simple_stack_behavior(self):
        sut = Stack[int]()

        assert sut.is_empty() is True

        sut.push(10)
        sut.push(20)
        sut.push(30)

        assert sut.peek() == 30
        assert sut.pop() == 30
        assert len(sut) == 2
