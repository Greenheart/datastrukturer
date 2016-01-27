"""Övningar på de enklare ADTerna."""

from .exceptions import EmptyStack, EmptyQueue


class Stack():
    """Implementation av ADTn stack.
    """

    def __init__(self):
        """Initierar en tom stack.
        """
        self.content = []

    def push(self, item):
        """Lägg till `item` överst på stacken.
        """
        self.content.insert(0, item)
        return True

    def pop(self):
        """Plockar bort och returnerar översta värdet på stacken.
        """
        if self.is_empty():
            raise EmptyStack

        return self.content.pop(0)

    def peek(self):
        """Returnerar översta värdet på stacken.
        """
        if self.is_empty():
            raise EmptyStack

        return self.content[0]

    def is_empty(self):
        """Returnerar `True` om stacken är tom, annars `False`.
        """
        return len(self.content) == 0

    def size(self):
        """Returnerar antalet värden på stacken.
        """
        return len(self.content)


class Queue():
    """Implementation av ADTn kö (queue).
    """

    def __init__(self):
        """Initierar en tom kö.
        """
        self.content = []

    def enqueue(self, item):
        """Lägger till `ìtem` i slutuet på kön.
        """
        self.content.append(item)
        return True

    def dequeue(self):
        """Plockar bort det första värdet i kön och returnerar det.
        """
        if self.is_empty():
            raise EmptyQueue

        return self.content.pop(0)

    def is_empty(self):
        """Returnerar `True` om kön är tom, annars `False`.
        """
        return len(self.content) == 0

    def size(self):
        """Returnerar antalet värden i kön.
        """
        return len(self.content)
