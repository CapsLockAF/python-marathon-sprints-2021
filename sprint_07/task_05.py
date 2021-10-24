# Imagine we are studying an organizational structure which consists of
# General Managers, Managers, and Developers. A General Manager may have
# many Managers working under him and a Manager may have many developers
# under him. Suppose, you have to determine the total salary of
# all the employees.
#
# One of the best solutions to the above-described problem is using
# Composite Method by working with a common interface that declares
# a method for calculating the total salary.
# Note.
#
# We attempt to make an organizational hierarchy with sub-organization,
# which may have subsequent sub-organizations, such as:
# GeneralManager                                   [Composite]
#       Manager1                                   [Composite]
#               Developer11                        [Leaf]
#               Developer12                        [Leaf]
#       Manager2                                   [Composite]
#               Developer21                        [Leaf]
#               Developer22                        [Leaf]
from abc import ABC, abstractmethod


class Component(ABC):
    _count = 0

    def add(self, child) -> None:
        pass

    def remove(self, child) -> None:
        pass

    @abstractmethod
    def showDetails(self) -> str:
        """
        The base Component may implement some default behavior or leave it to
        concrete classes (by declaring the method containing the behavior as
        "abstract").
        """
        pass


class LeafElement(Component):

    def __init__(self, *args):
        ''''Takes the first positional argument and assigns to member variable "position".'''
        self.position = args[0]

    def showDetails(self):
        '''Prints the position of the child element.'''
        print(Component._count * "\t" + self.position)


class CompositeElement(Component):

    def __init__(self, *args):
        '''Takes the first positional argument and assigns to member
         variable "position". Initializes a list of children elements.'''
        self.position = args[0]
        self._children = []


    def add(self, child):
        '''Adds the supplied child element to the list of children
         elements "children".'''
        self._children.append(child)

    def remove(self, child):
        '''Removes the supplied child element from the list of
        children elements "children".'''
        self._children.remove(child)

    def showDetails(self):
        '''Prints the details of the component element first. Then,
        iterates over each of its children, prints their details by
        calling their showDetails() method.'''

        print("\t" * Component._count + self.position)

        if "_children" in self.__dict__:
            Component._count = Component._count + 1
        for child in self._children:
            child.showDetails()
        Component._count = Component._count - 1
