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
        return self.content.pop(0)

    def peek(self):
        """Returnerar översta värdet på stacken.
        """
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
        pass

    def enqueue(self, item):
        """Lägger till `ìtem` i slutuet på kön.
        """
        pass

    def dequeue(self):
        """Plockar bort det första värdet i kön och returnerar det.
        """
        pass

    def is_empty(self):
        """Returnerar `True` om kön är tom, annars `False`.
        """
        pass

    def size(self):
        """Returnerar antalet värden i kön.
        """
        pass
