class Node:
    """
    Класс для узла стека
    """
    def __init__(self, data, next_node=None):
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

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека
        """
        node = Node(data)
        node.next_node = self.top
        self.top = node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения
        """
        data = self.top.data
        self.top = self.top.next_node
        return data
