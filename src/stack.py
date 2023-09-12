class Node:
    """
    Класс для узла стека
    """
    def __init__(self, data, next_node):
        """
        Конструктор класса Node
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """
    Класс для стека
    """
    def __init__(self):
        """
        Конструктор класса Stack
        """
        self.top = None

    def push(self, data) -> None:
        """
        Метод для добавления элемента на вершину стека
        """
        next_node = self.top
        new_top = Node(data, next_node)
        self.top = new_top
