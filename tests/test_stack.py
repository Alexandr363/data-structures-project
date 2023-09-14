"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Node, Stack


def test_init_node():
    node = Node('Тарелка', 15)
    assert node.data == 'Тарелка'


def test_init_stack():
    stack = Stack()
    assert stack.top is None


def test_stack_push():
    stack = Stack()
    stack.push(000)
    assert stack.top.data == 000


def test_stack_pop():
    stack = Stack()
    stack.push(000)
    stack.push(111)
    stack.pop()
    assert stack.top.data == 000
