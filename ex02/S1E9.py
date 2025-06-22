from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract base class for all characters in the GOT universe.
    Contains basic properties like first name and life status.
    """

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor for the Character class.
        :param first_name: The name of the character.
        :param is_alive: Boolean indicating if the character is alive.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Method to change the character's state to dead.
        Must be implemented by subclasses.
        """
        pass


class Stark(Character):
    """
    Stark family class inheriting from Character.
    Represents any Stark character in GOT.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor for Stark class.
        Initializes first_name and is_alive from parent.
        :param first_name: Name of the Stark character.
        :param is_alive: Whether the character is alive or not.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        Marks the character as dead by setting is_alive to False.
        """
        self.is_alive = False
