"""Övningar på ADTn unordered list."""

from .exceptions import EmptyList


class Node():
    """Implementation av nod för `UnorderedList`."""

    def __init__(self, data, next):
        """Initiera noden med attributen `self.data` och `self.next`."""
        self.data = data
        self.next = next


class UnorderedList():
    """Implementation av ADTn oordnad lista (unordered list).

    Listans första element har index 0.
    """

    def __init__(self):
        """Initiera den tomma listan."""
        self.head = None

    def is_empty(self):
        """Returnerar `True` om listan är tom, annars `False`."""
        return self.head is None

    def add(self, item):
        """Lägg till `item` i början av listan."""
        self.head = Node(item, self.head)

    def size(self):
        """Returnerar antalet värden i listan."""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def search(self, item):
        """Returnerar `True` om `item` finns i listan, annars `False`."""
        current = self.head
        while current:
            if current.data is item:
                return True
            current = current.next

        return False

    def remove(self, item):
        """Raderar första förekomsten av `item` från listan."""
        if self.is_empty():
            raise EmptyList

        current = self.head
        prev = None
        while current:
            if current.data == item:
                if prev:    # If we have a node before the current item
                    if current.next:
                        prev.next = current.next
                    else:
                        prev.next = None
                else:
                    self.head = current.next
                return True

            prev = current
            current = current.next

        return False

    def append(self, item):
        """Lägg till `item` i slutet av listan."""
        current = self.head

        if not current:  # List is empty
            self.head = Node(item, None)
            return True

        while True:
            if not current.next:
                current.next = Node(item, None)
                return True

            current = current.next

    def insert(self, position, item):
        """Lägg till `item` på index `position`."""
        current = self.head

        if position > self.size():
            raise IndexError

        # Only init these vars if actually needed
        index = 0
        prev = None

        while True:
            if index == position:
                if prev:  # Add between two existing items
                    prev.next = Node(item, current)
                    return True
                else:  # Add to the beginning
                    self.head = Node(item, current)
                    return True

            index += 1
            prev = current
            current = current.next

    def index(self, item):
        """Returnerar index i listan för första förekomsten av `item`."""
        if self.is_empty():
            raise EmptyList

        index = 0
        current = self.head
        while current:
            if current.data == item:
                return index

            current = current.next
            index += 1

        raise IndexError

    def pop(self, position=None):
        """Plockar bort och returnerar värdet på index `position`.

        Om inget värde anges för `position` tolkas det som sista värdet.
        """
        if self.is_empty():
            raise EmptyList
        # Verify that pos is valid if its given
        elif position and (position > self.size() - 1 or position < 0):
            raise IndexError
        elif self.size() == 1:
            data = self.head.data
            self.head = None
            return data

        current = self.head
        index = 0
        prev = None

        while True:
            if position == index:
                if prev:
                    if current.next:
                        prev.next = current.next
                    else:  # If last item is popped using index
                        prev.next = None
                else:  # If the first item is popped using index
                    self.head = current.next

                return current.data

            elif current.next:
                index += 1
                prev = current
                current = current.next

            # No pos given, pop last item
            elif not position and not current.next:
                prev.next = None
                return current.data

    def _vals(self):
        """Return a normal list with a copy of all present values."""
        if self.is_empty():
            raise EmptyList

        current = self.head
        vals = []

        while current:
            vals.append(current.data)
            current = current.next

        return vals
