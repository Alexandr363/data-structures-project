"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Node, Stack


def test_init_node():
    node = Node('Тарелка', 15)
    assert node.data == 'Тарелка'


def test_init_stack():
    stack = Stack()
    assert stack.top is None
