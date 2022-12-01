"""
    Nodo Class
    Luis Bodart A01635000
    https://github.com/Luis99B/Compiladores
"""


class Node:
    def __init__(self):
        self.type = ''
        self.val = ''
        self.childrens = []

    def __str__(self):
        return f'Nodo: {self.type}{f", val: {self.val}" if self.val != "" else ""}{f", childrens: {self.childrens}" if self.childrens else ""}'

    def __repr__(self):
        return f'Nodo: {self.type}{f", val: {self.val}" if self.val != "" else ""}{f", childrens: {self.childrens}" if self.childrens else ""}'

    def printTree(self, lvl=0):
        """
        It prints the type and value of the current node, then for each of its children,
        it calls the same function with an increased level

        :param lvl: The level of the tree, defaults to 0 (optional)
        """
        print(f"{' ' * lvl}{self.type} : {self.val}")
        for c in self.childrens:
            c.printTree(lvl + 1)
