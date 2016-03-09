"""Övningar på BinarySearchTree (BST).

Ett BST är ett rotat binärt träd där varje nod har en `key` och ett
eventuellt värde, `value`. Varje nod i trädet finns två träd,
`left` och `right`. En nods `key` måste vara större än alla noders `key`
i det vänstra trädet och mindre än alla noders `key` i det högra trädet.

Utseendet hos ett BST beror i väldigt hög grad på i vilken ordning noderna
lagts till. I värsta fall degenererar de fullständigt.

`Wikipedia <https://en.wikipedia.org/wiki/Binary_search_tree>`_
"""


class BinarySearchTree():
    """Implementation av BinarySearchTree (BST)."""

    def __init__(self, key, value=None):
        """Initiera det tomma trädet."""
        self.key = key
        self.left = None
        self.right = None
        self.value = value

    def insert(self, key, value=None):
        """Lägg till en nod i trädet."""
        if not self.lookup(key):  # Make sure that the key is unique
            node = self

            while node:
                if key < node.key:
                    if node.left:
                        node = node.left
                    else:
                        node.left = BinarySearchTree(key, value)
                        return True
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = BinarySearchTree(key, value)
                        return True

    def lookup(self, key):
        """Sök efter noden med matchande key.

        Returnerar matchande noden eller None.
        """
        if key == self.key:
            return (self.key, self.value)

        if key < self.key:
            if self.left:
                return self.left.lookup(key)
        else:
            if self.right:
                return self.right.lookup(key)

        return None

    def delete(self, key, parent=None):
        """Radera noden med matchande key."""
        # Get node with highest value to the left of the node2delete
        # Or node with lowest value to the right of the node2delete
        # Use any of these nodes as the new node instead of the node2delete

        if key == self.key:
            number_of_children = 0
            if self.left:
                number_of_children += 1
            if self.right:
                number_of_children += 1

            if number_of_children == 0:  # 0 children
                if parent.left == self:
                    parent.left = None
                else:
                    parent.right = None

            elif number_of_children == 1:  # 1 child
                if self.left is not None:  # We have a child to the left
                    new_node = self.left
                else:                      # We have a child to the right
                    new_node = self.right

                # Update parent's pointer
                if parent.left == self:
                    parent.left = new_node
                else:
                    parent.right = new_node

            elif number_of_children == 2:  # 2 children
                # 1. find node with
                    # a. highest key to the left of self or
                    # b. lowest key to the right of self
                # 2. set pointer of parent.left or parent.right to node

                # follow self.left of self.right to find right replacement-node
                successor = self.right
                successor_parent = self
                while successor.left:
                    successor_parent = successor
                    successor = successor.left

                if parent:
                    # Modify pointers so current will fit in it's new spot
                    successor.left = self.left
                    successor.right = self.right

                    # Update parent's pointer
                    if parent.left == self:
                        parent.left = successor
                    else:
                        parent.right = successor

                else:
                    self.key = successor.key
                    self.value = successor.value

                # Delete old position
                if successor_parent.left == successor:
                    successor_parent.left = None
                else:
                    successor_parent.right = None

            return True  # Hopefully a success

        # If we still need to find the right node to delete
        if key < self.key:
            if self.left:
                return self.left.delete(key, self)
        else:
            if self.right:
                return self.right.delete(key, self)

        return False

    def traverse(self):
        """En in-order traversering av trädets noder.

        Implementera som en generator.
        """
        if self.left:
            for node in self.left.traverse():
                yield node

        yield self

        if self.right:
            for node in self.right.traverse():
                yield node

    def __str__(self):
        """Utskrift av trädets alla noder (in-order)."""
        return ', '.join([str(x.key) for x in self.traverse()])
