"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack

test = Stack()


class TestStack(unittest.TestCase):
    def test_push(self):
        self.assertEqual(test.push(10), test.stack[0])
