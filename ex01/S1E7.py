from S1E9 import Character


class Baratheon(Character):
    """
    Representing the Baratheon family.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor for Baratheon class.
        Initializes first_name and is_alive from parent.
        :param first_name: Name of the Baratheon character.
        :param is_alive: Whether the character is alive or not.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """
        Marks the character as dead by setting is_alive to False.
        """
        self.is_alive = False

    def __str__(self):
        """ String representation of the Baratheon character. """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Technical representation."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """
    Representing the Lannister family.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor for a Lannister character.

        Args:
            first_name (str): Character's first name.
            is_alive (bool): Character's life status.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Sets the character's is_alive status to False."""
        self.is_alive = False

    def __str__(self):
        """String representation."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Technical representation."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """
        Class method to create a new Lannister.

        Args:
            first_name (str): Name of the Lannister.
            is_alive (bool): Life status.

        Returns:
            Lannister: A new Lannister object.
        """
        return cls(first_name, is_alive)
