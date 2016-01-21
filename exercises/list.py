"""Övningar på ADTn unordered list."""

from .exceptions import EmptyList

# TODO: maybe raise EmptyList if list is empty when methods try to access?
#       Or keep normal error handling code?


class Node():
    """Implementation av nod för `UnorderedList`.
    """

    def __init__(self, data, next):
        """Initiera noden med attributen `self.data` och `self.next`.
        """
        self.data = data
        self.next = next


class UnorderedList():
    """Implementation av ADTn oordnad lista (unordered list).

    Listans första element har index 0.
    """

    def __init__(self):
        """Initiera den tomma listan.
        """
        self.head = None

    def is_empty(self):
        """Returnerar `True` om listan är tom, annars `False`.
        """
        return self.head is None

    def add(self, item):
        """Lägg till `item` i början av listan.
        """
        self.head = Node(item, self.head)

    def size(self):
        """Returnerar antalet värden i listan.
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def search(self, item):
        """Returnerar `True` om `item` finns i listan, annars `False`.
        """
        current = self.head
        while current:
            if current.data is item:
                return True
            current = current.next

        return False

    def remove(self, item):
        """Raderar första förekomsten av `item` från listan.
        """
        current = self.head
        prev = None
        while current:
            if current.data == item:
                if prev:    # If we have a node before the current item
                    prev.next = current.next
                else:
                    self.head = current.next
                return True

            prev = current
            current = current.next

        return False    # Failure

    def append(self, item):
        """Lägg till `item` i slutet av listan.
        """
        current = self.head

        if not current:  # List is empty
            self.head = Node(item, None)
            return True

        while current:
            if not current.next:
                current.next = Node(item, None)
                return True

            current = current.next

    def insert(self, position, item):
        """Lägg till `item` på index `position`.
        """
        current = self.head

        if not current:  # No previous item, add to the beginning
            self.head = Node(item, None)
            return True

        # Only init these vars if actually needed
        index = 0
        prev = None

        while current:
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

        return False

    def index(self, item):
        """Returnerar index i listan för första förekomsten av `item`.
        """
        if not self.is_empty():
            index = 0
            current = self.head
            while current:
                if current.data == item:
                    return index

                current = current.next
                index += 1

        return None

    def pop(self, position=None):
        """Plockar bort och returnerar värdet på index `position`.

        Om inget värde anges för `position` tolkas det som sista värdet.
        """
        current = self.head

        if not current:  # List empty, nothing to pop
            return False
        elif position and (position > self.size() - 1 or position < 0):
            return False  # Invalid position

        # Only init these vars if actually needed
        index = 0
        prev = None

        while current:
            if isinstance(position, int) and position == index:
                if prev:
                    prev.next = current.next
                    return True
                else:  # No previous item, remove from beginning
                    if self.size() > 1:
                        self.head = current.next
                    else:
                        self.head = None

                    return True
            else:  # No pos given, just pop last item
                if not current.next:
                    if prev:
                        prev.next = None
                        return True
                    else:  # Only one item in list
                        self.head = None
                        return True

            index += 1
            prev = current
            current = current.next

    def _vals(self):
        """Returns a normal list with a copy of all present values
        """
        if not self.is_empty():
            current = self.head
            vals = []

            while current:
                vals.append(current.data)
                current = current.next

            return vals
